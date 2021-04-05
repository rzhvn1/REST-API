from django.urls import path
from .views import *

urlpatterns = [
    path('', RateView.as_view()),
    path('<int:worker_id>/', RateWorkerView.as_view()),
]