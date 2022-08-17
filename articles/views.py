from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, TemplateView
from django.views.generic.edit import CreateView, UpdateView # new
from .models import Articles
from django.urls import reverse_lazy

# Create your views here.
class ArticleListView(ListView):
    model = Articles
    template_name = 'home.html'

class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'article_detail.html'

    def get_object(self):
        obj = super().get_object()
        obj.blog_view += 1
        obj.save()
        return obj

class ArticleCreateView(CreateView):
    model = Articles
    template_name = 'article_new.html'
    fields = ['title','author', 'body','image' ]

class ArticleUpdateView(UpdateView):
    model= Articles
    fields = ['title', 'author', 'body', 'image']
    template_name = 'article_update.html'

class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('home')

# User faqat o'zi yozgan maqolalarni ko'rish uchun 
# Maqolalarim qismi uchun
def user_profile(request):
    skills = Articles.objects.filter(author__username = request.user)[::-1]
    return (request, "my_articles.html", {'skills' : skills})

