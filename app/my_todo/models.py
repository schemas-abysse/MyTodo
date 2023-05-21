from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TodoList(models.Model):
    todo_title = models.CharField(max_length=200)
    todo_text = models.TextField(null=True, blank=True)
