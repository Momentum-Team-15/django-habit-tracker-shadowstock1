from unicodedata import name
from django.conf import settings
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField

# Create your models here.

class User(AbstractUser):
    pass

class Habit(models.Model):
    name = models.CharField(max_length=50)
    metric = models.PositiveIntegerField()
    unit_of_measure = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='habits', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}"

class DailyRecord(models.Model):
    habit=models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='records')
    date=models.DateField(null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='records', null=True, blank=True)
    amount_completed=models.IntegerField(null=True)
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=['habit', 'date', 'user'], name ='unique_constraint')
        ]

    def percentage(self):
        return int((self.amount_completed / self.habit.metric) * 100)

    def __str__(self):
        return str(self.amount_completed)
