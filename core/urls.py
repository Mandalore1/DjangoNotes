from django.urls import path
import core.views as views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('notes/', views.notes_list_view, name="notes"),
    path('notes/<int:pk>', views.notes_detail_view, name="note"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
]
