import django.forms as forms
from django.contrib.auth.models import User

from account.models import UserAdditionalInfo


class RegisterForm(forms.Form):
    """Форма регистрации"""
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password_confirmation = forms.CharField(label="Подтверждение пароля",
                                            widget=forms.PasswordInput(attrs={"class": "form-control"}))


class LoginForm(forms.Form):
    """Форма входа"""
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserMainInfoForm(forms.ModelForm):
    """Основная информация о пользователе"""
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"})
        }
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "email": "Адрес электронной почты",
        }


class UserAdditionalInfoForm(forms.ModelForm):
    """Дополнительная информация о пользователе"""
    class Meta:
        model = UserAdditionalInfo
        fields = ["avatar", "about", "date_of_birth", "place"]
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "about": forms.Textarea(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control"}),
            "place": forms.TextInput(attrs={"class": "form-control"})
        }
