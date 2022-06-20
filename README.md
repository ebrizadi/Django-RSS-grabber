# Django RSS Grabber

A project in django to gather news in 'news' table, from a list of RSS urls added previously in a table named 'rss'. This script will be run every hour to gather new news in 'news' table.

## setup

Install **requirements** with 
```pip install -r requirements.txt```

Create a **superuser**

Add the sites that you want to read;
>Example : http://www.npr.org/rss/rss.php?id=1012  ---- as npr

## start celery

Open another terminal in your project and run:
```celery -A config worker -l info -B```

## How to use
Once the setup is done and your server is running, **every hour** the news will update.
Also you can always add new sources to reading expected news.
