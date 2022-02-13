from django.urls import path
from . import views
 

urlpatterns = [
    path('',views.home, name="home"),
    path('webdevelopment/', views.webdevelopment, name="webdevelopment"),
    # path('appdevelopment/', views.appdevelopment, name="appdevelopment"),
    path('technews/', views.technews, name="technews"),

    path('contact/', views.contact, name="contact"),

]