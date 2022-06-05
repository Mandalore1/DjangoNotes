from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import DatabaseError
from django.shortcuts import render, redirect, get_object_or_404

from account.forms import LoginForm, RegisterForm, UserMainInfoForm, UserAdditionalInfoForm


def user_info_view(request, username):
    """Контроллер просмотра информации о пользователе"""
    if request.method == "GET":
        user = get_object_or_404(User, username=username)
        return render(request, "user_info.html", {"user": user})


@login_required
def user_info_update_view(request, username):
    """Контроллер изменения информации о пользователе"""
    user = get_object_or_404(User, username=username)
    if request.user != user:
        return redirect("home")
    main_info_form = UserMainInfoForm(instance=user)
    additional_info_form = UserAdditionalInfoForm(instance=user.additional_info)

    if request.method == "GET":
        return render(request, "user_info_update.html",
                      {"main_info_form": main_info_form, "additional_info_form": additional_info_form})

    if request.method == "POST":
        try:
            info_type = request.GET["info_type"]
        except KeyError:
            messages.error(request, "Не указан тип формы")
            return render(request, "user_info_update.html",
                          {"main_info_form": main_info_form, "additional_info_form": additional_info_form})

        if info_type == "main":
            main_info_form = UserMainInfoForm(request.POST, instance=user)
            if main_info_form.is_valid():
                main_info_form.save()
                messages.success(request, "Данные обновлены успешно")
                return render(request, "user_info_update.html",
                              {"main_info_form": main_info_form, "additional_info_form": additional_info_form})
            else:
                messages.error(request, "Введенные данные имели неверный формат!")
                return render(request, "user_info_update.html",
                              {"main_info_form": main_info_form, "additional_info_form": additional_info_form})

        elif info_type == "additional":
            additional_info_form = UserAdditionalInfoForm(request.POST, request.FILES, instance=user.additional_info)
            if additional_info_form.is_valid():
                additional_info_form.save()
                messages.success(request, "Данные обновлены успешно")
                return render(request, "user_info_update.html",
                              {"main_info_form": main_info_form, "additional_info_form": additional_info_form})
            else:
                messages.error(request, "Введенные данные имели неверный формат!")
                return render(request, "user_info_update.html",
                              {"main_info_form": main_info_form, "additional_info_form": additional_info_form})

        else:
            messages.error(request, "Не указан тип формы")
            return render(request, "user_info_update.html",
                          {"main_info_form": main_info_form, "additional_info_form": additional_info_form})


def login_view(request):
    """Контроллер входа пользователя в аккаунт"""
    login_form = None

    if request.method == "GET":
        login_form = LoginForm()

    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data["username"],
                                password=login_form.cleaned_data["password"])
            if user is not None:
                login(request, user)

                # Если пользователь попал на страницу логина с другой страницы,
                # перенаправляем его на изначальную страницу
                if "next" in request.GET:
                    return redirect(request.GET["next"])

                # Иначе перенаправляем его на главную страницу
                return redirect("home")
            else:
                messages.error(request, "Неправильное имя пользователя или пароль")
        else:
            messages.error(request, "Данные имели неверный формат")

    return render(request, "login.html", {"form": login_form})


def logout_view(request):
    """Контроллер выхода пользователя из аккаунта"""
    logout(request)
    return redirect("login")


def register_view(request):
    """Контроллер регистрации пользователя"""
    register_form = None

    if request.method == "GET":
        register_form = RegisterForm()

    if request.method == "POST":
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            if register_form.cleaned_data["password"] != register_form.cleaned_data["password_confirmation"]:
                messages.error(request, "Пароль и подтверждение пароля не совпадают!")
                return render(request, "register.html", {"form": register_form})

            same_username = User.objects.filter(username=register_form.cleaned_data["username"]).exists()
            if same_username:
                messages.error(request, "Имя пользователя уже существует!")
                return render(request, "register.html", {"form": register_form})

            try:
                user = User.objects.create_user(register_form.cleaned_data["username"],
                                                register_form.cleaned_data["email"],
                                                register_form.cleaned_data["password"])
            except DatabaseError:
                messages.error(request, "Не удалось зарегистрироваться!")
                return render(request, "register.html", {"form": register_form})
            else:
                login(request, user)
                messages.success(request, "Вы успешно зарегистрировались!")
                return redirect("home")
        else:
            messages.error(request, "Данные имели неверный формат")

    return render(request, "register.html", {"form": register_form})
