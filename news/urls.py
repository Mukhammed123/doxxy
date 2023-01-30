from django.urls import path
from .views import news_view, news_detail_view

urlpatterns = [
    path('<str:pk>/', news_detail_view),
    path('', news_view),
]