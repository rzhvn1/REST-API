from django.urls import path
from .views import *

urlpatterns = [
    path('', RestaurantProfileView.as_view()),
    path('table/', TableView.as_view()),
    path('table/<int:table_id>/', TableDetailView.as_view()),
    path('userprofile/', UserProfileView.as_view()),

]