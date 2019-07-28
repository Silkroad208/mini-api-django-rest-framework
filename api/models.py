from django.db import models

# Create your models here.


class Department(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Employee(models.Model):

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname
