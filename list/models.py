from datetime import datetime
from django.db import models

# Create your models here.

class Todo_List(models.Model):
    username = models.CharField(max_length=30)
    title = models.TextField()
    complete = models.BooleanField(default=False)
    # slug = models.CharField(max_length=20)
    # time = models.DateTimeField(now = True)

    def __str__(self):
        return self.username
