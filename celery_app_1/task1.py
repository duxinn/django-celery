from __future__ import absolute_import
import time
from .celery import app


@app.task
def myadd(x, y):
    time.sleep(1)
    return x + y
