from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Slider, Plan
from django.utils.html import format_html

# Register your models here.

class sliderAdmin(admin.ModelAdmin):
    
    def sliderPhoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('headline', 'sliderPhoto')

admin.site.register(Slider, sliderAdmin)




class planAdmin(admin.ModelAdmin):
    list_display = ('plan_types','originalprice','price','discountpercent')

admin.site.register(Plan,planAdmin)

