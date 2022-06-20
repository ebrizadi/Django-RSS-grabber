from django.db import models


class RSS(models.Model):
    site_name = models.CharField(
        verbose_name='Site', max_length=20
    )

    link = models.URLField(
        verbose_name='Link', max_length=500,
        null=True, blank=True,
        )
    
    class Meta:
        verbose_name_plural = 'RSS resources'

    def __str__(self):
        return self.site_name


class News(models.Model):
    rss = models.ForeignKey(
        RSS, related_name='news',
        verbose_name='News', on_delete=models.CASCADE
        )

    title = models.TextField(
        verbose_name='News Title',
        null=True, blank=True,
    )

    summary = models.TextField(
        verbose_name='News Summary',
        null=True, blank=True,
    )

    published_at = models.DateTimeField(
        verbose_name='Publiched Date',
        null=True
        )
    
    class Meta:
        verbose_name_plural = 'News list'

    def __str__(self):
        return self.title


    