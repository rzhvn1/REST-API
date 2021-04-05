from rest_framework import serializers
from .models import *
from order.serializers import OrderSerializer
from order.models import Order

class RestaurantProfileSerializer(serializers.ModelSerializer):

    salary = serializers.IntegerField(read_only=True)

    class Meta:
        model = RestaurantProfile
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = '__all__'

class TableDetailSerializer(serializers.ModelSerializer):

    order = OrderSerializer(many=True)

    class Meta:
        model = Table
        fields = ['id', 'area', 'status', 'order']

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'

class CardCreateSerializers(serializers.Serializer):
    number = serializers.IntegerField()
    date = serializers.DateField()
    holder = serializers.CharField(max_length=20)
    code = serializers.IntegerField(min_value=100, max_value=999)



class UserProfileSerializer(serializers.ModelSerializer):

    cards = CardSerializer(many=True)
    bonuses = serializers.IntegerField(read_only=True)
    order_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'full_name', 'street', 'house', 'bonuses', 'order_count', 'email', 'cards']



