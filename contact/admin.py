from django.contrib import admin
from .models import Contact
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('first_name','phone','email','company','subject')
    search_fields = ('first_name','phone','email','company','subject','message')
admin.site.register(Contact,contactAdmin)
