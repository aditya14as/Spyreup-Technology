from django.contrib import admin
from .models import Order
# Register your models here.
class orderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone','plan','amount', 'paid', 'created_date')
    search_fields = ('name','email','phone')
    list_filter = ('paid','plan')
    list_display_links = ('name','email','phone')
    
admin.site.register(Order,orderAdmin)