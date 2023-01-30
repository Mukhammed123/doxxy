from django.db import models

class News(models.Model):
    slug = models.SlugField(unique=True)
    en_title = models.CharField(max_length=255, verbose_name='Title (en)')
    en_body = models.TextField(verbose_name='Body (en)')
    de_title = models.CharField(max_length=255, verbose_name='Titel (de)')
    de_body = models.TextField(verbose_name='Körper (de)')
    fr_title = models.CharField(max_length=255, verbose_name='Titre (fr)')
    fr_body = models.TextField(verbose_name='Corps (fr)')

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.slug
