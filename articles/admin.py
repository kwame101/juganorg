from django.contrib import admin
from . models import Article
# Register your models here.

#register the article model in admin panel
admin.site.register(Article)
