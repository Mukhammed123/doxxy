from django.db import models

class News(models.Model):
    slug = models.SlugField(unique=True)
    fr_title = models.CharField(max_length=255)
    fr_body = models.TextField()
    de_title = models.CharField(max_length=255)
    de_body = models.TextField()
    en_title = models.CharField(max_length=255)
    en_body = models.TextField()

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.slug
