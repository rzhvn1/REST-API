from django.db import models
from accounts.models import RestaurantProfile, UserProfile

class Rate(models.Model):
    worker = models.ForeignKey(RestaurantProfile, on_delete=models.SET_NULL, null=True)
    star = models.PositiveIntegerField(default=None, null=True)
    date_created = models.DateField(auto_now_add=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


