from django.shortcuts import render
from newsapi import NewsApiClient
import requests
API_KEY = '{API_KEY}'

# Create your views here.
def technews(request):
    url = f'https://newsapi.org/v2/top-headlines?category=technology&country=in&country=us&apiKey={API_KEY}'
    response =requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {
        'articles':articles
    }
    return render(request,'webpages/news/homenews.html', context)

