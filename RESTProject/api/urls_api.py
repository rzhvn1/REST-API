from django.urls import path
from .views import *

urlpatterns = [
    path('hard/', MealViewHard.as_view()),
    path('', MealView.as_view()),
    path('<int:meal_id>/', MealDetailView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<str:category_name>/', CategoryDetailView.as_view()),
]