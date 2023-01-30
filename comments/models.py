from django.db import models
from pages.models import Page
from news.models import News

language_choices = (
    ('fr', 'French'),
    ('de', 'German'),
    ('en', 'English'),
)

class Comment(models.Model):
    language = models.CharField(max_length=2, choices=language_choices, default='en')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    page = models.ForeignKey(Page, related_name='page_comments', on_delete=models.CASCADE, null=True, blank=True)
    news = models.ForeignKey(News, related_name='news_comments', on_delete=models.CASCADE, null=True, blank=True)
