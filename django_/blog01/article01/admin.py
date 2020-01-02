from django.contrib import admin

# Register your models here.

from article01.models import Article
# from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    articles = Article
    list_display = ('name', 'timestamp')
    list_filter = ('timestamp',)


admin.site.register(Article, ArticleAdmin)


