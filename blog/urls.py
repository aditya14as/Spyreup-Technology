from django.urls import path
from . import views
 

urlpatterns = [
    path(" ",views.blog, name="blog"),
    path("blogpost/<int:id>",views.blogpost, name="blogpost"),
   
]