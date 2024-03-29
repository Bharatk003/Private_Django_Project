from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
from .models import Post
class BlogListView(ListView):

    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):

    model = Post
    template_name = 'post_detail.html'

    #in DetailView there is the context_object_name = object/post, it is default for the DetailView
    #context_object only gives us an access to the one object at a time as per the primary key (pk )

class BlogCreateView(CreateView):

    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):

    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']


class BlogDeleteView(DeleteView):

    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


 