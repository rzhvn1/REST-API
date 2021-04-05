from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import views, status
from order.services import salary_increase, count_worker_orders
from django.contrib.auth.models import User

class RestaurantProfileView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            profile = RestaurantProfile.objects.get(user=request.user)
        except RestaurantProfile.DoesNotExist:
            return Response({"data":"Profile Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RestaurantProfileSerializer(profile)
        count_worker_orders(profile.id)
        salary_increase(profile.id)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        profile = RestaurantProfile.objects.get(user=request.user)
        serializer = RestaurantProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"SUCCESSFULLY UPDATED!!!"})
        return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        profile = RestaurantProfile.objects.get(user=request.user)
        profile.delete()
        return Response({"data":"OK!"})

class TableView(views.APIView):

    def get(self, request, *args, **kwargs):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)

class TableDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            table = Table.objects.get(id = kwargs['table_id'])
        except Table.DoesNotExist:
            return Response({"data":"Table Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TableDetailSerializer(table)
        return Response(serializer.data)




class UserProfileView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except TypeError:
            return Response({"data":"Profile Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except TypeError:
            return Response({"data":"Profile Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CardCreateSerializers(data=request.data)
        if serializer.is_valid():
            number = serializer.data.get('number')
            holder = serializer.data.get('holder')
            date = serializer.data.get('date')
            code = serializer.data.get('code')
            Card.objects.create(profile=profile, number=number, holder_name=holder, date=date, code=code)
            return Response({"CARD ADDED SUCCESFULLY!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)




