from django.shortcuts import render
from rest_framework import views, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .models import *
from .services import use_promo, get_pay, salary_increase
from .serializers import *
from accounts.services import *
from .services import use_promo
from django.utils import timezone


class OrderView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    # def get_pay(self, obj):
    #     card = obj.user.userprofile.cards.filter(status='default')[0]
    #     if obj.payment_type == 'card' and obj.status != 'closed':
    #         try:
    #             card.balance -= obj.total_price
    #             card.save()
    #             obj.status = 'Closed'
    #             obj.save()
    #         except IntegrityError:
    #             raise ValidationError('Not enough money!')


    def post(self, request, *args, **kwargs):

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # user = serializer.data.get('user')
            # count_orders(user)
            order_id = serializer.data.get('id')
            try:
                profile = RestaurantProfile.objects.get(user=request.user)
            except RestaurantProfile.DoesNotExist:
                profile = UserProfile.objects.get(user=request.user)
            if isinstance(profile, RestaurantProfile):
                order = Order.objects.get(id=order_id)
                order.worker = request.user.restaurantprofile
                order.save()
            total_sum = serializer.data.get('total_sum')
            get_pay(order_id)
            # count_bonuses(user, total_sum)
            return Response({"data":"OK!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class ModifyOrderView(views.APIView):

    def put(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['order_id'])
        order_minute, order_hour = order.date_created.minute, order.date_created.hour * 60
        current_minute, current_hour = timezone.now().minute, timezone.now().hour * 60
        order_time = order_minute + order_hour
        current_time = current_minute + current_hour
        abs_value = abs(current_time - order_time)

        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            if abs_value <= 5 and order.status == 'In process':
                serializer.save()
                return Response({"data":"order updated successfully!"})
            return Response({"data":f"time is up or order is {order.status}"})
        return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['order_id'])
        order_minute, order_hour = order.date_created.minute, order.date_created.hour * 60
        current_minute, current_hour = timezone.now().minute, timezone.now().hour * 60
        order_time = order_minute + order_hour
        current_time = current_minute + current_hour
        abs_value = abs(current_time - order_time)
        if abs_value <= 5 and order.status == 'In process':
            order.delete()
            return Response("order is cancelled!")
        return Response(f"Time is up or order is {order.status}")


class AdminUserPutOrder(views.APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, *args, **kwargs):
        try:
            order = Order.objects.get(id=kwargs['order_id'], status__in=['In process', 'Ready'])
        except Order.DoesNotExist:
            return Response(f"Order not found or order closed!", status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['order_id'], status__in=['In process', 'Ready'])
        serializer = CloseOrderSerializer(data=request.data)
        if serializer.is_valid():
            guest_money = serializer.data.get('guest_money')
            if guest_money >= order.total_price:
                change = guest_money - order.total_price
                order.status = serializer.data.get('new_status')
                order.save()
                return Response(f"Your change: {change}", status=status.HTTP_200_OK)
            return Response("not enough money", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)