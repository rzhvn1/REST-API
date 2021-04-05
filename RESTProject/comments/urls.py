from django.urls import path
from .views import *
from api.views import MealDetailView

urlpatterns = [
    path('<int:meal_id>/', MealDetailView.as_view()),

]