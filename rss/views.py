from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .serializers import NewsListSerializer
from .models import RSS, News


class NewsListAPIView(ListAPIView):
    serializer_class = NewsListSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return News.objects.all().order_by('published_at')
    
