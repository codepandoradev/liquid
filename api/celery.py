import os

from celery import Celery
from celery.signals import after_task_publish
from celery import shared_task

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")

app = Celery('api')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@after_task_publish.connect
def update_sent_state(sender=None, headers=None, **_):
    task = app.tasks.get(sender)
    backend = task.backend if task else app.backend
    backend.store_result(headers['id'], None, 'SENT')


@app.task(bind=True)
def debug_task(self):
    pass # here debug
    
    
@shared_task(name="repeat_order_make")
def repeat_order_make(order_id):
    print('Статус получен!')
    

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(1, test.s('hello'), name='add every 1')
    
    
@app.task
def test(arg):
    print(arg)
