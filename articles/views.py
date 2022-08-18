from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, TemplateView
from django.views.generic.edit import CreateView, UpdateView # new
from .models import Articles
from django.urls import reverse_lazy
from .const import Const

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class ArticleListView(ListView):
    model = Articles
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView,self).get_context_data(**kwargs)
        context["regions"] = dict(Const.regions)
        context['categories'] = dict(Const.categories)

        return context
    



class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'article_detail.html'

    def get_context_date(self, **kwargs):
        context = super(ArticlesDetailView,self).get_context_data(**kwargs)
        context['articles'] = Articles.objects.all()
        return context

    def get_object(self):
        obj = super().get_object()
        obj.blog_view += 1
        obj.save()
        return obj

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Articles
    template_name = 'article_new.html'
    fields = ['title', 'body','image', 'region', 'category' ]

    # tekshiruv, Muallifni avto aniqlaydi
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(). form_valid(form)  

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user  

class ArticleUpdateView(UserPassesTestMixin,LoginRequiredMixin, UpdateView):
    model= Articles
    fields = ['title', 'body', 'image', 'region', 'category']
    template_name = 'article_update.html'

    # tekshiruv, Muallifni avto aniqlaydi
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(). form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 

class ArticleDeleteView(UserPassesTestMixin ,LoginRequiredMixin,DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('home')

    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 

# User faqat o'zi yozgan maqolalarni ko'rish uchun 
# Maqolalarim qismi uchun
def user_profile(request):
    skills = Articles.objects.filter(author__username = request.user)[::-1]
    return render(request, "my_articles.html", {'skills' : skills})

# regions 
def ArticleRegionListView(request, pk):
    region = dict(Const.regions)[pk]
    object_list = Articles.objects.filter(region=pk)[::-1]
    context = {
        "object_list": object_list,
        "region": region
    }

    return render(request, 'region_filter.html', context)

# Category
def ArticleCategoryListView(request, pk):
    category = dict(Const.categories)[pk]
    object_list = Articles.objects.filter(category=pk)[::-1]
    context = {
        "object_list": object_list,
        "category": category
    }

    return render(request, 'category_filter.html', context)

