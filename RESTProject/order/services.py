from django.db import IntegrityError
from .models import Promocode, Order
from accounts.models import RestaurantProfile
from django.utils import timezone
from rest_framework.exceptions import ValidationError

#TODO
def use_promo(order_id, promocode):
    order = Order.objects.get(id=order_id)
    promo_list = Promocode.objects.filter(status='active', end_date__gt=timezone.now())

    for promo in promo_list:
        if promo.code == promocode:
            order.total_price = order.total_price - order.total_price * promo.sale
            order.save()
    return order.total_price

def get_pay(order_id):
    order = Order.objects.get(id=order_id)
    promo_price = use_promo(order_id, order.promocode)
    card = order.userprofile.cards.filter(status='default')[0]
    if order.payment_type == 'card' and order.status != 'closed':
        try:
            card.balance -= promo_price
            card.save()
            order.status = 'Closed'
            order.save()
        except IntegrityError:
            raise ValidationError('Not enough money!')
    order.total_price = promo_price
    order.save()

def count_worker_orders(worker_id):
    worker = RestaurantProfile.objects.get(id=worker_id)
    worker_order_lst = Order.objects.filter(worker=worker, status='Closed')
    worker.order_count = len(worker_order_lst)
    worker.save()



def salary_increase(worker_id):
    worker = RestaurantProfile.objects.get(id=worker_id)
    if worker.order_count == 100:
        worker.salary += 5000
        worker.save()
    elif worker.order_count == 200:
        worker.salary += 10000
        worker.save()








