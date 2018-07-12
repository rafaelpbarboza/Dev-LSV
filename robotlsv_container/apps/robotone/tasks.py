from __future__ import unicode_literals, absolute_import # for unicode and python 2.7

# importando celery
import datetime

# import
import xlsxwriter as xlsxwriter

from apps.robotone.Robots import RobotElUniversal, RobotElTiempo
from robotlsv import celery_app as app
from celery import group, chain, chord

# importar modelos
from .models import Robotmintor

# impor for email task
from django.conf import settings
from django.core.mail import EmailMessage, send_mail

from celery.signals import after_task_publish


@after_task_publish.connect
def task_sent_handler(sender=None, headers=None, body=None, **kwargs):
    info = headers if 'task' in headers else body
    print('after_task_publish for task id {info[id]}'.format(
        info=info,
    ))







# @app.task(bind=True)
# def initrobot(self, robo_id, kwords, pagination=0):
#     """inicializar y redireccionar el tipo de robot"""
#
#     # get robot type by id = type
#     current_robot = Robotmintor.objects.get(pk=robo_id)
#     # print("robot type 1: {}".format(current_robot.type))
#     robo_type = current_robot.TYPE[int(current_robot.type)-1][1]
#
#     # inicializar valor de started
#     current_robot.started = datetime.datetime.now()
#     current_robot.status = "2"
#     current_robot.save()
#
#     # print("robot type 2: {}".format(robo_type))
#
#     if robo_type == 'robotA':
#         robot_type_news.delay(robo_id, kwords, pagination)
#     else:
#         return "You have no set up {} tyoe fo robot yet".format(robo_type)
#
# # this is a robo type.
# @app.task()
# def robot_type_news(robot_id, keywords, pagination):
#     print("TEST: Robot type executed")
#
#     chord(
#         group(
#             robot_news_eluniversal.s(robot_id, keywords, pagination),
#             robot_news_eltiempo.s(robot_id, keywords, pagination)
#         )  # add all the task for this type in here
#     )(
#         chain(save_to_excel.s() | send_email.s())
#     )
#
# # robo universal
# @app.task()
# def robot_news_eluniversal(robot_id, keywords, pagination):
#
#     # RobotElTiempo('Palbra1 palabra2', 5)
#     robot = RobotElUniversal(keywords, pagination)
#     news = robot.run()
#
#     print("TEST: Robot universal terminated")
#     return news
#
# # robo el tiempo
# @app.task()
# def robot_news_eltiempo(robot_id, keywords, pagination):
#
#     robot = RobotElTiempo(keywords, pagination)
#     news = robot.run()
#     print("TEST: Robot el tiempo terminated")
#     return news
#
# @app.task
# def save_to_excel(data):
#     print("Excel task execute")
#     print("This is the data type that the chrod funct send {}".format(type(data)))
#
#     # test
#     # file_data = open('media/data.py', "a")
#     # file_data.write(str(data))
#     # file_data.close()
#
#     file_path = 'media/links.xlsx'
#     file_headers = ['News title', 'Link', 'News paper']
#
#     workbook = xlsxwriter.Workbook(file_path)
#     worksheet = workbook.add_worksheet()
#     worksheet.write_row(0, 0, file_headers)
#
#     row, col = 1, 0
#     for news_per_newspaper in data:
#         for individual_news in news_per_newspaper:
#             worksheet.write_row(row, col, individual_news)
#             row += 1
#
#     workbook.close()
#     print("file has been created in {}".format(file_path))
#     return file_path
#
# @app.task()
# def send_email(file_path):
#     print("email task started")
#     subject = "your subcject"
#     body = "your body"
#
#     e = EmailMessage()
#     e.subject = subject
#     e.to = settings.EMAIL_RECIPIENTS_LIST
#     e.body = body
#     e.attach_file(file_path)
#     e.send()
#
#     print(settings.EMAIL_RECIPIENTS_LIST)
#
#     print("emil test was passed the file path: {}".format(file_path))
