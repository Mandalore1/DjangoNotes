import django.forms as forms

from core.models import Note


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


class NoteForm(forms.ModelForm):
    """Форма записки"""
    class Meta:
        model = Note
        fields = ["title", "text", "image", "user"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "user": forms.HiddenInput()
        }
