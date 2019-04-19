from __future__ import absolute_import

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from celery import shared_task, task
from celery.utils.log import get_logger
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import logging



LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
pro = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
f = os.path.join(pro, 'log', app)
logging.basicConfig(filename=f'{f}.log',
                    level=logging.INFO, format=LOG_FORMAT)
log = logging.getLogger('index')


'''
'_log', '_process_aware', '_signal_safe', 'addFilter', 'addHandler', 'callHandlers', 'critical', 'debug', 'disabled', 'error', 'exception', 'fatal', 'filter', 'filters', 'findCaller', 'getChild', 'getEffectiveLevel', 'handle', 'handlers', 'hasHandlers', 'info', 'isEnabledFor', 'level', 'log', 'makeRecord', 'manager', 'name', 'parent', 'propagate', 
'removeFilter', 'removeHandler', 'root', 'setLevel', 'warn', 
'warning'
'''


@csrf_exempt
@shared_task()
def add(x, y):
    print("%d + %d = %d" % (x, y, x + y))
    log.info(f'add will running')
    log.info(f'add ran ok')
    return x + y


@csrf_exempt
@shared_task()
def mul(x, y):
    print("%d * %d = %d" % (x, y, x * y))
    log.info(f'add will running')
    log.info(f'add ran ok')
    return x * y


@csrf_exempt
@shared_task()
def sub(x, y):
    print("%d - %d = %d" % (x, y, x - y))
    return x - y


@csrf_exempt
@shared_task()
def just_print():
    print("Print from celery task")
    return "Print from celery task"
