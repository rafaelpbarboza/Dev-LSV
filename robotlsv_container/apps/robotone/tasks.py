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


@app.task(bind=True)
def initrobot(self, robo_id, kwords, pagination=5):
    """inicializar y redireccionar el tipo de robot"""

    # get robot type by id = type
    current_robot = Robotmintor.objects.get(pk=robo_id)
    robo_type =  current_robot.TYPE[int(current_robot.type)][1]

    # inicializar valor de started
    current_robot.started = datetime.datetime.now()
    current_robot.status = "2"
    current_robot.save()

    print("robot type: {}".format(robo_type))

    if robo_type == 'robotB':
        robot_type_news.delay(robo_id, kwords)

# # # this is a robo type.
@app.task()
def robot_type_news(robot_id, keywords):
    print("TEST: Robot type executed")

    chord(
        group(robot_news_eluniversal.s(robot_id, keywords))  # add all the task for this type in here
    )(
        chain(save_to_excel.s() | send_email.s())
    )

# robo universal
@app.task()
def robot_news_eluniversal(robot_id, keywords):
    print("TEST: Robot universal executed")
    news_universal = RobotElUniversal(keywords)
    return news_universal

# robo el tiempo
@app.task()
def robot_news_eltiempo():
    return print("se ejecuto el tiempo")

@app.task
def save_to_excel(data):
    # print("Excel task execute, This is the data passed to it:\n{}".format(data))

    # test
    # file_data = open('media/data.py', "a")
    # file_data.write(str(data))
    # file_data.close()

    file_path = 'media/links.xlsx'
    file_headers = ['News title', 'Link']

    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()
    worksheet.write_row(0, 0, file_headers)

    row, col = 1, 0
    for individual_news in data[0]:
        worksheet.write_row(row, col, individual_news)
        row += 1

    workbook.close()
    print("file has been created in {}".format(file_path))
    return file_path

@app.task()
def send_email(file_path):
    print("email task")
    subject = "your subcject"
    body = "your body"

    e = EmailMessage()
    e.subject = subject
    e.to = settings.EMAIL_RECIPIENTS_LIST
    e.body = body
    e.attach_file(file_path)
    e.send()

    print(settings.EMAIL_RECIPIENTS_LIST)

    print("emil test was passed the file path: {}".format(file_path))
