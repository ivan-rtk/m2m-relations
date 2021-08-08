from django.shortcuts import render
#from django.views.generic import ListView
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().prefetch_related('scopes')

    context = {
        'object_list': articles
    }

    return render(request, template, context)
