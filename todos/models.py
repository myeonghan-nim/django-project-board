from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    content = models.TextField()
    due_date = models.DateField()
