from sqlite3 import Date

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import initrobot
# Create your views here.
from rest_framework.viewsets import ModelViewSet
# from apps.robotone.models import MonitorizatorRobot
# from apps.robotone.serializers import RobotoneSerializers
from .models import Robotmintor
from .serializers import RobotoneSerializers, UserSerializer, PostSerializer


class RobotModelViewSet(ModelViewSet):
    queryset = Robotmintor.objects.all()
    serializer_class = RobotoneSerializers

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# test view


class Robot_view(APIView):

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            data=serializer.data
            try:
                user=User.objects.get(id=data['id'])
                initrobot.delay(user.id,data['word'],data['page'])
                #return Response(serializer.data, status=status.HTTP_200_OK)
                return HttpResponseRedirect('../model/'+str(user.id))
            except Exception:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                print(Exception.message)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



