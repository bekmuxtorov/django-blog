from unicodedata import category
from django.contrib import admin
from django.urls import path,include

from . import views

from . import views
urlpatterns = [
    path('regions/<str:pk>/', views.ArticleRegionListView, name="regions"),
    path('categry/<str:pk>/', views.ArticleCategoryListView, name="categories"),
    path('mening_maqolalarim/', views.user_profile, name="my_articles"),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('article/new/', views.ArticleCreateView.as_view(), name='article_new'),
    path('article/<int:pk>/', views.ArticlesDetailView.as_view(), name='article_detail'),

    
    path('', views.ArticleListView.as_view(), name='home'),

    
]
