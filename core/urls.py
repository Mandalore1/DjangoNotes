from django.urls import path
import core.views as views

urlpatterns = [
    path('test/', views.test_view, name="test"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
