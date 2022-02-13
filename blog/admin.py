from django.contrib import admin
from .models import Blog
from .models import *
from tinymce.widgets import TinyMCE
from django.utils.html import format_html
from django.contrib.admin.decorators import display


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField : { 'widget': TinyMCE()},
    }

    def blogPhoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('title','writter','blogPhoto')
    search_fields = ('title','writter','heading','content')
    list_filter = ('writter',)

admin.site.register(Blog, BlogAdmin)
