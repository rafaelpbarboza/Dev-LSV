from __future__ import unicode_literals, absolute_import # for unicode and python 2.7

# importando celery
from robotlsv import celery_app as app

# importar recursos

@app.task()
def prueba():
    print("Se ejecuto prueba task")
