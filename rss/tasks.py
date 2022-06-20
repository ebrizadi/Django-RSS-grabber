from datetime import datetime
from time import mktime
from celery import shared_task
from celery.utils.log import get_task_logger
import feedparser
from .models import RSS, News

logger = get_task_logger(__name__)


@shared_task
def update_news():
    try:
        rss_list = RSS.objects.all()
        for rss in rss_list:
            url = rss.link
            feed = feedparser.parse(url) #Parsing XML data
            if feed['entries']:
                for entry in feed['entries']:
                    news, created = News.objects.get_or_create(
                        rss=rss,
                        title=entry['title'],
                        published_at=datetime.fromtimestamp(mktime(entry['published_parsed']))
                    )
                    if created:
                        news.summary = entry['summary']
                        news.save()
    except:
        logger.exception('Error in connecting rss feed!')

    