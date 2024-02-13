from django.shortcuts import render

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from todo_api.serializers import UserSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse



def test_api (request):
    test = {'test':1}
    return JsonResponse(test)
    


