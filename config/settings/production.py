from .base import *

CELERY_BROKER_URL = "redis://aminco.ir/redis"
CELERY_RESULT_BACKEND = "redis://aminco.ir/redis"


from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "update_news": {
        "task": "rss.tasks.update_news",
        "schedule": crontab(hour="*/1"),
    },
}
