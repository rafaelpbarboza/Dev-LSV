from django.http import HttpResponse
from django.shortcuts import render
from apps.robotone import tasks

# Create your views here.


def index(request):
    tasks.initrobot.delay('1', 'portal dulces barrio')
    return HttpResponse('holaaaaaaa')