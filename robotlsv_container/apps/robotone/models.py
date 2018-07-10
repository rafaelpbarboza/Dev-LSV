from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class MonitorizatorRobot(models.Model):
    started = models.DateTimeField()
    finished = models.DateTimeField()
    response = models.CharField(max_length=250)
    TYPE = (
        ('RobotA''', 'robotA'),
        ('RobotB', 'robotB')
    )
    type = models.CharField(choices=TYPE, default=1, max_length=50)
    STATE = (
        ('Waiting', 'waiting'),
        ('Working', 'working'),
        ('Finished', 'finished')
    )
    status = models.CharField(choices=STATE, default=1,  max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
