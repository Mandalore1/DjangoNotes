from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Note(models.Model):
    """Класс записки"""
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст", blank=True, null=True)
    image = models.ImageField(upload_to="note_images", verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes", verbose_name="Пользователь")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Записка"
        verbose_name_plural = "Записки"
