from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Comment
from .form import CommentForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    )
# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.urls import reverse_lazy,reverse

class ArticleListView(LoginRequiredMixin, ListView):

    model =  Article
    template_name = 'article_list.html'
    login_url = 'login'
    
    # context_object_name = 'article_list'

class ArticleDetailView(LoginRequiredMixin, DetailView):

    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):

    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):

    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = Article
    template_name = 'article_new.html'
    # success_url = reverse_lazy('article_detail')
    fields = ('title','body')

    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


 
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'article_comment.html'
    # success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        article_id = self.kwargs['pk']
        form.instance.article_id = article_id
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        article_id = self.kwargs.get('pk')
        return reverse_lazy('article_detail', kwargs={'pk': article_id})

     

