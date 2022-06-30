from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Tasks(models.Model):
        class Meta:
            ordering = ['complete']
            verbose_name = 'Задача'
            verbose_name_plural = 'Задачи'

        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
        title = models.CharField(max_length=200)
        description = models.TextField(null=True, blank=True)
        complete = models.BooleanField(default=False)
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title

