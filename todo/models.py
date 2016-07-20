from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    description = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.description