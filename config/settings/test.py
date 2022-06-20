from .base import *

CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"


from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "update_news": {
        "task": "rss.tasks.update_news",
        "schedule": crontab(hour="*/1"),
    },
}

