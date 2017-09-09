from django.db import models

class Todos(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title
