from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import DatabaseError
from django.shortcuts import render, redirect, get_object_or_404

from .forms import LoginForm, RegisterForm, NoteForm
from .models import Note


# Create your views here.


def home_view(request):
    """Контроллер главной страницы"""
    if request.method == "GET":
        return render(request, "home.html")


@login_required
def notes_list_view(request):
    """Контроллер списка записок пользователя"""
    if request.method == "GET":
        user = request.user
        notes = user.notes.all()
        return render(request, "notes_list.html", {"notes": notes})


@login_required
def notes_detail_view(request, pk):
    """Контроллер детализированного представления записки"""
    if request.method == "GET":
        note = get_object_or_404(Note, pk=pk)

        if note.user != request.user:
            return redirect("home")

        return render(request, "notes_detail.html", {"note": note})


@login_required
def notes_add_view(request):
    """Контроллер создания записки"""
    form = None

    if request.method == "GET":
        form = NoteForm()
        form.fields["user"].initial = request.user
        return render(request, "notes_add.html", {"form": form})

    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            # Если вписали не своего пользователя
            if request.user != form.cleaned_data["user"]:
                return redirect("home")

            note = form.save()
            return redirect("note", pk=note.pk)
        else:
            messages.error(request, "Введенные данные имели неверный формат!")
            return render(request, "notes_add.html", {"form": form})


@login_required
def notes_update_view(request, pk):
    """Контроллер изменения записки"""
    note = get_object_or_404(Note, pk=pk)
    form = None

    if request.method == "GET":
        form = NoteForm(instance=note)
        return render(request, "notes_update.html", {"form": form, "note": note})

    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            # Если вписали не своего пользователя
            if request.user != form.cleaned_data["user"]:
                return redirect("home")

            note = form.save()
            return redirect("note", pk=note.pk)
        else:
            messages.error(request, "Введенные данные имели неверный формат!")
            return render(request, "notes_add.html", {"form": form, "note": note})


@login_required
def notes_delete_view(request, pk):
    """Контроллер удаления записки"""
    note = get_object_or_404(Note, pk=pk)
    if note.user != request.user:
        return redirect("home")

    if request.method == "GET":
        return render(request, "notes_confirm_delete.html", {"note": note})

    if request.method == "POST":
        note.delete()
        messages.success(request, "Записка успешно удалена!")
        return redirect("notes")


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
