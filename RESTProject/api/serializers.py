from rest_framework import serializers
from .models import *

class MealSerializerHard(serializers.Serializer):
    portions = (
        ('0.7', '0.7'),
        ('1', '1')
    )
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=200)
    price = serializers.IntegerField(min_value=0)
    portion = serializers.ChoiceField(choices=portions)

class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

class CategoryDetailSerializer(serializers.ModelSerializer):

    meal_set = MealSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'meal_set']

    def create(self, validated_data):
        meal_data = validated_data.pop('meal_set')
        category = Category.objects.create(**validated_data)
        for meal in meal_data:
            Meal.objects.create(category=category, **meal)
        return category
