from django.shortcuts import render
from .models import Blog
# Create your views here.
def blog(request):
    myposts = Blog.objects.order_by('-pub_date').all()
    return render(request, 'webpages/blog/homeblog.html',{'myposts': myposts})

def blogpost(request,id):
    post = Blog.objects.filter(post_id =id)[0]
    return render(request, 'webpages/blog/blogpost.html', {'post': post})