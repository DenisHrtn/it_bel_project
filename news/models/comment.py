from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone

from .like import Like
from .news import News
from users.models.user import User


class Comment(models.Model):
    comment_id = models.AutoField(
        primary_key=True,
        verbose_name='ID комментария',
    )
    text = models.TextField(
        max_length=300,
        verbose_name='Текст комментария',
    )
    added = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата добавления',
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Какой пользователь оставил',
        null=True,
        blank=True,
    )
    likes = GenericRelation(Like)

    def __str__(self) -> str:
        return self.text

    @property
    def total_likes(self) -> int:
        return self.likes.count()

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий"
        ordering = ['-added']
