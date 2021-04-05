from django.contrib.auth.models import User
from order.models import Order

def count_orders(user_id):
    user = User.objects.get(id=user_id)
    user.userprofile.order_count += 1
    user.userprofile.save()

def count_bonuses(user_id, total_sum):
    user = User.objects.get(id=user_id)
    user.userprofile.bonuses += total_sum * 0.1
    user.userprofile.save()




