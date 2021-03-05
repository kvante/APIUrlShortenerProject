
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404, redirect

from .models import URL
from .Serializers import URLSerializer, URLListSerializer


class MyPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UrlCreateView(CreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer


class UrlListView(ListAPIView):
    queryset = URL.objects.all()
    serializer_class = URLListSerializer
    pagination_class = MyPagination


def root(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    url.clicked()

    return redirect(url.full_url)
