from django.shortcuts import render
from .models import Article
# Create your views here.
from django.views.generic import ListView

class ArticleListView(ListView):

    template_name = 'article_list.html'
    model =  Article
    # context_object_name = 'article_list'