import django.forms as forms


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