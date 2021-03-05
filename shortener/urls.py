from django.urls import path

from .views import UrlCreateView, UrlListView

app_name = 'shortener'


urlpatterns = [
    path('stream/create', UrlCreateView.as_view()),
    path('stream/URLllist', UrlListView.as_view()),


]
