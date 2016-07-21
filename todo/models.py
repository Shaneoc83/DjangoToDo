from __future__ import unicode_literals

from django.db import models
from accounts.models import User


# Create your models here.
class ToDoItem(models.Model):
    description = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.description
