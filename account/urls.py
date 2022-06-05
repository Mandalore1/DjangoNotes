from django.urls import path

import account.views as views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('user/<slug:username>/', views.user_info_view, name="user_info"),
    path('user/<slug:username>/update/', views.user_info_update_view, name="user_info_update"),
    path('user/<slug:username>/update/main-info', views.user_main_info_update_view, name="user_main_info_update"),
    path('user/<slug:username>/update/additional-info', views.user_additional_info_update_view,
         name="user_additional_info_update")
]
