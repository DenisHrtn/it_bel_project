from django.db import models
from django.utils import timezone

class Author(models.Model): 
    """Модель автора""" 
 
    author_id = models.PositiveIntegerField( 
        primary_key=True, 
        verbose_name="ID автора" 
    ) 
 
    author_name = models.CharField( 
        max_length=150, 
        verbose_name="Ник" 
    ) 
 
    name = models.CharField( 
        max_length=150,  
        verbose_name="Имя", 
        unique=True 
    ) 
 
    surname = models.CharField( 
        max_length=150,  
        verbose_name="Фамилия" 
    ) 
 
    age = models.PositiveIntegerField( 
        verbose_name="Возраст"
    ) 
 
    email = models.EmailField() 
 
    date_joined = models.DateField( 
        verbose_name="Дата регистрации", 
        default=timezone.now 
    ) 
 
    is_active = models.BooleanField( 
        verbose_name="Активный", 
        default=True 
    ) 
 
    class Meta: 
        verbose_name = "Автор" 
        verbose_name_plural = "Авторы"