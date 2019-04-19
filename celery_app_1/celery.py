# -*- coding: utf-8 -*-

from celery import Celery

app = Celery('app_1', backend="amqp")  # 创建 Celery 实例
app.config_from_object('celery_app_1.celeryconfig')
