from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language
from django.db.models import F
from .models import News
from comments.models import Comment

def news_view(request):
    language = get_language()
    news = News.objects.only('slug')
    if language == 'fr':
        news = news.annotate(title=F('fr_title'), body=F('fr_body'))
    elif language == 'de':
        news = news.annotate(title=F('de_title'), body=F('de_body'))
    else:
        news = news.annotate(title=F('en_title'), body=F('en_body'))

    return render(request, 'news.html', {'data': news})

def news_detail_view(request, slug):
    language = get_language()

    instance = get_object_or_404(News, slug=slug)

    comments = Comment.objects.filter(news=instance, language=language)

    context = {
        'instance': instance,
        'comments': comments,
        'language': language,
        }

    return render(request, 'details.html', context)
