from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
# from apps.robotone.models import MonitorizatorRobot
# from apps.robotone.serializers import RobotoneSerializers
from .models import MonitorizatorRobot
from .serializers import RobotoneSerializers


class RobotModelViewSet(ModelViewSet):
    queryset = MonitorizatorRobot.objects.all()
    serializer_class = RobotoneSerializers

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

