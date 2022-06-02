import django.forms as forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
