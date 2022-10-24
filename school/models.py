from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    rg = models.CharField(max_length=9)

    def __str__(self):
        return self.name
