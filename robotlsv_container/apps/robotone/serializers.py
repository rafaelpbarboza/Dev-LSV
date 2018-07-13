from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Robotmintor


class UserSerializer(serializers.ModelSerializer):
    #monitorizatorrobot = serializers.PrimaryKeyRelatedField(many=True, queryset=MonitorizatorRobot.objects.all())
    class Meta:
        model = User
        fields = ('username', 'password') #, 'monitorizatorrobot'


class RobotoneSerializers(serializers.ModelSerializer):
   # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Robotmintor
        fields = ('started', 'finished', 'response', 'type', 'status', 'user')


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    word = serializers.CharField(required=True, max_length=100)
    # type=serializers.CharField(required=True)
    page=serializers.IntegerField(required=True)
    method=serializers.IntegerField(required=True)