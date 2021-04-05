from django.urls import path, include
from .views import *
urlpatterns = [
    path('', OrderView.as_view()),
    path('<int:order_id>/', ModifyOrderView.as_view()),
    path('close/<int:order_id>/', AdminUserPutOrder.as_view()),
]