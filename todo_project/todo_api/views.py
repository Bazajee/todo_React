from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import Group, User
from rest_framework.response import Response


from rest_framework import generics

from todo_api.serializers import UserSerializer, TaskListSerializer, TasksSerializer
from todo_api.models import User, TaskList, Task


class allLists(generics.ListAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    
    
class allTasks(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    


