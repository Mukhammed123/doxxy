from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language
from .models import Page

def pages_view(request, slug):
    language = get_language()

    queryset = get_object_or_404(Page, slug=slug)

    return render(request, 'details.html', {'instance': queryset, 'language': language})