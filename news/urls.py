from django.urls import path
from .views import news_view, news_detail_view

urlpatterns = [
    path('<slug:slug>/', news_detail_view, name='news-detail'),
    path('', news_view, name='news'),
]