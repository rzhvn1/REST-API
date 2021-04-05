from django.contrib import admin
from .models import *

admin.site.register([RestaurantProfile, Table, UserProfile, Card])
