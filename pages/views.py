from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language
from .models import Page
from comments.models import Comment

def pages_view(request, slug):
    language = get_language()

    instance = get_object_or_404(Page, slug=slug)

    comments = Comment.objects.filter(page=instance, language=language)

    context = {
        'instance': instance,
        'comments': comments,
        'language': language,
        }

    return render(request, 'details.html', context)