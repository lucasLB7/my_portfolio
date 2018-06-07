from django.contrib import admin
from .models import Editor, Article, Category, github_link



class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('category','github_link')



admin.site.register(Editor)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(github_link)



