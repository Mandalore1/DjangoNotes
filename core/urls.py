from django.urls import path

import core.views as views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('notes/', views.notes_list_view, name="notes"),
    path('notes/<int:pk>', views.notes_detail_view, name="note"),
    path('notes/add', views.notes_add_view, name="note_add"),
    path('notes/update/<int:pk>', views.notes_update_view, name="note_update"),
    path('notes/delete/<int:pk>', views.notes_delete_view, name="note_delete"),
    path('notes/add-favorite/<int:pk>', views.notes_favorite_view, name="note_favorite"),
]
