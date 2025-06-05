from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)





