from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserAdditionalInfo(models.Model):
    """Дополнительная информация о пользователе"""
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="additional_info",
                                verbose_name="Пользователь")
    avatar = models.ImageField(upload_to="user_avatars", verbose_name="Аватар", blank=True, null=True)
    about = models.TextField(verbose_name="О себе", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    place = models.CharField(max_length=150, verbose_name="Место проживания", blank=True, null=True)

    def __str__(self):
        return f"Дополнительная информация о {self.user.username}"

    class Meta:
        verbose_name = "Дополнительная информация о пользователе"
        verbose_name_plural = "Дополнительная информация о пользователях"
