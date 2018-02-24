from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    #add author

    #return title on each article instead of an object
    def __str__(self):
        return self.title

    def snippet(self):
        #extract 50 chars from body str
        return self.body[:50] + '...'
