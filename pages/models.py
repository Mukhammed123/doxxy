from django.db import models

class Page(models.Model):
    slug = models.SlugField(unique=True)
    en_title = models.CharField(max_length=255)
    en_body = models.TextField()
    de_title = models.CharField(max_length=255)
    de_body = models.TextField()
    fr_title = models.CharField(max_length=255)
    fr_body = models.TextField()

    def __str__(self):
        return self.slug
    
    # def get_absolute_url(self):
    #     return reverse()