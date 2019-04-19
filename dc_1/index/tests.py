import os

from django.test import TestCase

# Create your tests here.

s = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(s)
# /home/duxin/work/celery_test/django_celery_demo/dc_1
# print(__file__)
# s = '/home/duxin/work/celery_test/django_celery_demo/dc_1/index/tests.py'
# print(os.path.basename(os.path.dirname(s)))
# print(os.path.basename(s))

# /home/duxin/work/celery_test/django_celery_demo/dc_1/index
# tests.py
pro = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(pro, 'log', app))



