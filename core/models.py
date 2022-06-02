from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    text = models.TextField(blank=True, verbose_name="Текст")
    image = models.ImageField(upload_to="note_images", verbose_name="Изображение", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", verbose_name="Пользователь")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"
