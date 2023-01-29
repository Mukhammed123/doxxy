from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language, activate
from .models import Page

def pages_view(request, slug):
    language = get_language()

    queryset = Page.objects.get(slug=slug)

    return render(request, 'page.html', {'instance': queryset.__dict__, 'language': language})