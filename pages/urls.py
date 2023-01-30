from django.urls import path
from .views import pages_view

urlpatterns = [
    path('<slug:slug>/', pages_view, 'pages'),
]