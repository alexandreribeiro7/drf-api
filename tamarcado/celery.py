from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tamarcado.settings.dev')

app = Celery('tamarcado')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

@app.task
def soma(a, b):
    return a + b
