from django.db import models

class Query(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    query = models.TextField()

    def __str__(self):
        return self.name
