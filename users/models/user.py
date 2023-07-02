from django.db import models
from django.utils import timezone

from ..managers.user import UserManager
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    """Модель пользователя"""

    user_id = models.AutoField(
        primary_key=True,
        verbose_name="ID пользователя"
    )
    username = models.CharField(
        verbose_name="Имя пользователя",
        max_length=150,
        unique=True,
        null=True,
        blank=True
    )
    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name="Почта пользователя",
        help_text="Email"
    )
    date_joined = models.DateTimeField(
        verbose_name="Дата регистрации",
        default=timezone.now
    )
    is_staff = models.BooleanField(
        verbose_name="Админ",
        default=False
    )
    is_active = models.BooleanField(
        verbose_name="Активный",
        default=True
    )

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return f"{self.username} ({self.email})"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"