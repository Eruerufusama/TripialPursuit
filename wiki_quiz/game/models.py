from django.db import models
from django.contrib.auth.models import User

class Query(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    query = models.TextField()

    def __str__(self):
        return self.name


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # session_key = models.CharField()
    category = models.CharField(max_length=20)
