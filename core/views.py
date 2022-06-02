from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm


# Create your views here.


def test_view(request):
    if request.method == "GET":
        return render(request, "test.html")


def login_view(request):
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
                return redirect("test")
            else:
                messages.error(request, "Неправильное имя пользователя или пароль")
        else:
            messages.error(request, "Данные имели неверный формат")

    return render(request, "login.html", {"form": login_form})


def logout_view(request):
    logout(request)
    return redirect("login")
