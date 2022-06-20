from dataclasses import fields
from rest_framework import serializers
from .models import RSS, News


class RSSListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSS
        fields = ('site_name', )

class RSSDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSS
        fields = ('site_name', 'link', )



class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('rss', 'title', )


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('rss', 'title', 'body', )