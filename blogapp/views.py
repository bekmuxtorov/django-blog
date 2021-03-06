from re import L
from turtle import title
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class BasePagesView(ListView):
    model = Post
    template_name = 'base.html'

class BlogDetailsView(DetailView):
    model = Post
    template_name = 'postitems.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
        