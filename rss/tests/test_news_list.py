from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key
from django.contrib.auth import get_user_model

from rss.models import RSS, News


User = get_user_model()

class TestNewsListAPIView(TestCase):

    def setUp(self):
        self.user = mommy.make(User, is_active=True, username='testuser', password='123456')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_get_news_list(self):
        rss = mommy.make(RSS)
        news_count = 3
        news_list = mommy.make(News, rss=rss, _quantity=news_count)
        url = reverse('news')
        response = self.client.get(url, fomat='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], news_count)
        for news in response.data['results']:
            self.assertEqual(news['rss'], rss.id)

