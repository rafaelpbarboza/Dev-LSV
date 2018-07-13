from sqlite3 import Date

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
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
    #Verificar si usuario tiene permisos y si esta autenticado
    permission_classes = (IsAuthenticated, )
    authentication_classes = (SessionAuthentication, BasicAuthentication)

#Capturamos el envio por post
    def post(self, request):
        #serializamos el request
        serializer = PostSerializer(data=request.data)
        #validamos que el serializador sea valido
        if serializer.is_valid():
            data = serializer.data
            monitor = get_object_or_404(Robotmintor.objects.filter(id=data['id']))
            if monitor.user.id == self.request.user.id:
                if data['method']==1:
                    initrobot.delay(monitor.id, data['word'], data['page'])
                    if monitor.status == "2" or monitor.status == "3":
                        return Response({'description': 'This monitor have been initiated or have been finished'},
                                        status=status.HTTP_403_FORBIDDEN)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif data['method']==2:
                    if monitor.status == "1" or monitor.status == "3":
                        return Response({'description': "This monitor can't be stopped"})
                    return Response(serializer.data, status=status.HTTP_200_OK)

                # If method 1 == Inicar and IF Monitor.stado == Iniciado => El monitor ya fue iniciado
            # IF method 2 == Detener
                #IF METHOD IS WAITING NO HAY NADA QUE DENETER
                #IF FINISHED YA ESTA DETENIDO
                #monitor.status


            else:
                return Response({'description':'You are not the owner of this monitor'}, status=status.HTTP_403_FORBIDDEN)

