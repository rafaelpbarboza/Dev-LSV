from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Robot(models.Model):
    started = models.DateTimeField()
    finished = models.DateTimeField()
    response = models.CharField(max_length=250)
    TYPE = (
        (1, 'robotA'),
        (2, 'robotB')
    )
    type = models.CharField(choices=TYPE, default=1, max_length=50)
    state = (
        (1, 'Waiting'),
        (2, 'Working'),
        (3, 'Finished'),
    )
    status = models.CharField(choices=state, default=1, max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __init__(self):
    #     self.status = 'Waiting'
