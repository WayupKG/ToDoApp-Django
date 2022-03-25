from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    title = models.CharField('Называние', max_length=250)
    end_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default="В ожидании")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ('-create_date',)


