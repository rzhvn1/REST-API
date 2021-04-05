from django.contrib.auth.models import User
from django.db import models

#TODO order_count
class RestaurantProfile(models.Model):
    #id
    full_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    date_start = models.DateField(auto_now_add=True)
    date_end = models.DateField(auto_now_add=True)
    salary = models.PositiveIntegerField(default=0)
    schedule = models.CharField(choices=(
                                            ('2/2', '2/2'),
                                            ('5/2', '5/2')
                                        ), max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    order_count = models.PositiveIntegerField(default=0)

class Table(models.Model):
    area = models.CharField(choices=(
                            ('Main', 'Main'),
                            ('Street', 'Street'),
                            ('VIP', 'VIP'),
                            ), max_length=50)
    status = models.CharField(choices=(
                            ('Reserved', 'Reserved'),
                            ('Free', 'Free'),
                            ), max_length=50)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    full_name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField(default=0)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=10)
    email = models.EmailField()
    bonuses = models.PositiveIntegerField(default=0, blank=True)
    order_count = models.PositiveIntegerField(default=0, blank=True)

class Card(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='cards')
    number = models.PositiveIntegerField(default=0)
    holder_name = models.CharField(max_length=50)
    date = models.DateField()
    code = models.IntegerField(default=0)
    balance = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=
                              (
                                  ('default', 'default'),
                                  ('non active', 'non active'),
                              ), max_length=15, default='non active')













