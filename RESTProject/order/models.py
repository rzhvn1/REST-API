from django.contrib.auth.models import User
from django.db import models
from api.models import Meal
from accounts.models import Table, UserProfile, RestaurantProfile

class Order(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    worker = models.ForeignKey(RestaurantProfile, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL,null=True, related_name='order')
    status = models.CharField(choices=
                                    (
                                        ('Ready', 'Ready'),
                                        ('In process', 'In process'),
                                        ('Closed', 'Closed')
                                    ), max_length=20, default='In process')
    payment_type = models.CharField(choices=
                                    (
                                        ('card', 'card'),
                                        ('cash', 'cash'),
                                    ), max_length=20, default='cash')
    promocode = models.CharField(max_length=10, blank=True, null=True, default='1')

class Promocode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    sale = models.FloatField(default=0.1)
    end_date = models.DateField()
    status = models.CharField(choices=
                              (
                                  ('active', 'active'),
                                  ('dead', 'dead'),
                              ), max_length=10, default='active')

    def __str__(self):
        return self.code + ' ' + self.status


class MealToOrder(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='MTO')
    quantity = models.PositiveIntegerField(default=1)





