from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Employee(models.Model):
    number = models.CharField(max_length = 20, verbose_name="Employee Number")
    firstname = models.CharField(max_length = 20, verbose_name= "First Name")
    lastname = models.CharField(max_length = 20, verbose_name= "Last Name")
    active = models.BooleanField(verbose_name="Employee Active")

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)

class Reward(models.Model):
    name = models.CharField(max_length = 20, verbose_name= "Name")
    description = models.CharField(max_length = 100, verbose_name= "Description")

    def __str__(self):
        return '{}'.format(self.name)

class Employee_Reward(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee', verbose_name="Employee")
    reward = models.ForeignKey(Reward,on_delete=models.CASCADE, related_name='reward', verbose_name="Reward")
    awarded_on = models.DateField(default=timezone.now, verbose_name='Awarded On')
    awarded_by = models.ForeignKey(User, default='', on_delete=models.CASCADE, related_name='user', verbose_name= "Awarded By")

    def __str__(self):
        return '{} - {}'.format(self.employee, self.reward)