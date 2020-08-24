from django.db import models


# superuser details: username - pagination, pw - web@12345
# Create your models here.

class Employee(models.Model):
    emp_id = models.IntegerField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    def __str__(self):
        return " {}".format(self.firstname)


class User(models.Model):
    user_id = models.IntegerField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    def __str__(self):
        return " {}".format(self.user_id)
