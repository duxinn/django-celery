# celeryconfig.py


# redis 127.0.0.1:6379


# 每秒10次
from datetime import timedelta

from celery.schedules import crontab

# CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '2/s'}}

# 低优先级
CELERY_ROUTES = {
    'tasks.add': 'low-priority',
}

# broker
# BROKER_URL = 'redis://127.0.0.1:6379/10'

# backend
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/11'

CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化和反序列化使用msgpack方案

CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显

CELERY_ACCEPT_CONTENT = ['json', 'msgpack']  # 指定接受的内容类型

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (  # 指定导入的任务模块
    'celery_app_1.task1',
    'celery_app_1.task2'
)

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'celery_app_1.task1.myadd',
        'schedule': timedelta(seconds=3),  # 每 30 秒执行一次
        'args': (1, 1)  # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_app_1.task2.mymul',
        'schedule': crontab(hour=9, minute=50),  # 每天早上 9 点 50 分执行一次
        'args': (1, 2)  # 任务函数参数
    }
}
