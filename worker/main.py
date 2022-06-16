from celery import Celery

BROKER_URL = 'redis://redis-broker:6379/0'
BACKEND_URL = 'redis://redis-backend:6380/0'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

@app.task(name='add')
def add(x, y):
    return x + y
