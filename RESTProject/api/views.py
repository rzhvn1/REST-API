from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import views, status
from comments.serializers import CommentHardSerializer
from comments.models import Comment
from rest_framework import permissions


class MealViewHard(views.APIView):

    def get(self, request, *args, **kwargs):
        meals = Meal.objects.all()
        serializer = MealSerializerHard(meals, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MealSerializerHard(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            description = serializer.data.get('description')
            price = serializer.data.get('price')
            portion = serializer.data.get('portion')
            Meal.objects.create(name=name, description=description, price=price,
                                portion=portion
                                )
            return Response({"data":"OK!"})
        return Response(serializer.errors)

class MealView(views.APIView):

    def get(self, request, *args, **kwargs):
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"OK!"}, status=status.HTTP_201_CREATED)

class MealDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            meal = Meal.objects.get(id=kwargs['meal_id'])
        except Meal.DoesNotExist:
            return Response({"data":"Meal Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MealSerializer(meal)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentHardSerializer(data=request.data)
        meal = Meal.objects.get(id=kwargs['meal_id'])
        profile = request.user.userprofile
        if serializer.is_valid():
            Comment.objects.create(text=serializer.data.get('text'), meal=meal, profile=profile)
            return Response({"data":"OK!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)



class CategoryView(views.APIView):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)



class CategoryDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            category = Category.objects.get(name = kwargs['category_name'])
        except Category.DoesNotExist:
            return Response({"data":"Category Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategoryDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"OK!"}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors)
