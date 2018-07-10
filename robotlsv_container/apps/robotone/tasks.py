from __future__ import unicode_literals, absolute_import # for unicode and python 2.7

# importando celery
import datetime
from pprint import pprint

from apps.robotone.Robots import robot_eluniversal
from robotlsv import celery_app as app
from celery import group, chain

# importar modelos
from .models import Robotmintor


@app.task(bind=True)
def initrobot(self, robo_id, kwords):
    """inicializar y redireccionar el tipo de robot"""

    # get robot type by id = type
    current_robot = Robotmintor.objects.get(pk=robo_id)
    robo_type =  current_robot.TYPE[int(current_robot.type)][1]

    # inicializar valor de started
    current_robot.started = datetime.datetime.now()
    current_robot.status = "2"
    current_robot.save()

    robot_news.delay(robo_id, kwords)


@app.task()
def robot_news(id, keywords):
    news = robot_eluniversal(keywords)
    pprint(news)

@app.task
def save_to_excel():
    pass

@app.task()
def send_email():
    pass