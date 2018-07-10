from __future__ import unicode_literals, absolute_import # for unicode and python 2.7

# importando celery
from robotlsv import celery_app as app
from celery import group, chain

# importar modelos
from .models import Robot


# jesus currently working on tasks
# @app.task(bind=True)
# def inirobot(self, robo_id, *args):
#     """inicializar y redireccionar el tipo de robot"""
#
#     # get robot type by id = type
#     current_robot = Robot.objects.get(pk=robo_id)
#     robo_tye =  current_robot.type
#
#     # inicializar valor de started
#     # setiar atributo de stado a working
#     if type:
#         robot_type.
#
#     robot_news.delay()
#     pass


# @app.task(bind=True)
# def robot_news(self):
#     robot1(keywords)

@app.task
def save_to_excel():
    pass

@app.task()
def send_email():
    pass