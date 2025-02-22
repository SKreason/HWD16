import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HW.settings')

app = Celery('HW')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_news_last_week': {
        'task': 'news.tasks.send_news_last_week',
        'schedule': crontab(hour='8', minute='0', day_of_week='mon'),
    },
}
