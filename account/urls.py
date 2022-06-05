from django.urls import path

import account.views as views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('user/<slug:username>', views.user_info_view, name="user_info")
]
