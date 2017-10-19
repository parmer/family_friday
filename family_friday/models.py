from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100, unique=True)
    join_date = models.DateTimeField()

    def __str__(self):
        return self.name

