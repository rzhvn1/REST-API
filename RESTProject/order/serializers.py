from django.db import IntegrityError
from rest_framework import serializers
from .services import use_promo
from .models import *

class MTOSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = MealToOrder
        fields = ['id', 'meal', 'quantity']


class OrderSerializer(serializers.ModelSerializer):

    status = serializers.CharField(read_only=True)
    total_price = serializers.IntegerField(min_value=0, read_only=True)
    total_sum = serializers.SerializerMethodField()
    MTO = MTOSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'table', 'date_created', 'status',
                  'total_price', 'total_sum', 'userprofile', 'worker', 'payment_type', 'promocode', 'MTO']


    def create(self, validated_data):
        mto_data = validated_data.pop('MTO')
        order = Order.objects.create(**validated_data)
        for mto in mto_data:
            drop_id = mto.pop('id')
            MealToOrder.objects.create(order=order, **mto)
        return order

    def update(self, instance, validated_data):
        instance.table = validated_data.get('table', instance.table)
        instance.payment_type = validated_data.get('payment_type', instance.payment_type)
        instance.promocode = validated_data.get('promocode', instance.promocode)
        instance.save()
        mto_data = validated_data.get('MTO')
        for mto in mto_data:
            mto_instance = MealToOrder.objects.get(id=mto.get('id'))
            mto_instance.meal = mto.get('meal', mto_instance.meal)
            mto_instance.quantity = mto.get('quantity', mto_instance.quantity)
            mto_instance.save()
        return instance




    def get_total_sum(self, obj):
        total_sum = 0
        for mto in obj.MTO.all():
            total_sum += mto.meal.price * mto.quantity
        obj.total_price = total_sum
        obj.save()
        return total_sum




        # promo_price = use_promo(obj.id, obj.promocode)
        # if obj.payment_type == 'card':
        #     card = obj.user.userprofile.cards.filter(status='default')[0]
        #     try:
        #         card.balance -= promo_price
        #         card.save()
        #     except IntegrityError:
        #         raise ValidationError('Not enough money!')


class CloseOrderSerializer(serializers.Serializer):
    new_status = serializers.ChoiceField(choices=(('Closed', 'Closed')))
    guest_money = serializers.IntegerField(min_value=0)









