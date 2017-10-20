from django.db import models


MIN_GROUP_SIZE = 3
MAX_GROUP_SIZE = 5


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100, unique=True)
    join_date = models.DateTimeField()

    def __str__(self):
        return self.name

