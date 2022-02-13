from django.contrib import admin
from .models import extendeduser

# Register your models here.
class extendeduserAdmin(admin.ModelAdmin):
    list_display = ('phone','user')

admin.site.register(extendeduser,extendeduserAdmin)

