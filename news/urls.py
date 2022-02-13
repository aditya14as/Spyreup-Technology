from django.urls import path
from . import views
 

urlpatterns = [
    path('',views.technews, name="technews"),

]