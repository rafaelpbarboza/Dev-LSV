from django.http import HttpResponse
from django.shortcuts import render
from apps.robotone import tasks
# Create your views here.
from rest_framework.viewsets import ModelViewSet
# from apps.robotone.models import MonitorizatorRobot
# from apps.robotone.serializers import RobotoneSerializers
from .models import Robotmintor
from .serializers import RobotoneSerializers


class RobotModelViewSet(ModelViewSet):
    queryset = Robotmintor.objects.all()
    serializer_class = RobotoneSerializers

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# test view
def robot_view(request):

    tasks.initrobot.delay(1, 'dulces del portal', 2)

    return HttpResponse('You called the task initrobot!')