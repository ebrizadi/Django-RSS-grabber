from django.urls import path, include
from . import views


urlpatterns = [
    path(
        'news/', 
        views.NewsListAPIView.as_view(),
        name='news',
        ),
]