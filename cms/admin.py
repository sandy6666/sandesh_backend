from django.contrib import admin
from .models import Page, Blog


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created', 'updated', 'author')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created', 'updated', 'author')


admin.site.register(Page, PageAdmin)
admin.site.register(Blog, BlogAdmin)
