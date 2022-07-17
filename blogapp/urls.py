from importlib.resources import path
from pathlib import Path
from unicodedata import name
from unittest.mock import patch
from django.urls import path
from .views import HomePageView, BasePagesView, BlogDetailsView,BlogCreateView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('base/', BasePagesView.as_view(), name = 'base'),
    path('post/<int:pk>/', BlogDetailsView.as_view(), name = 'post_detail' ),
    path('post/new/', BlogCreateView.as_view(), name = 'post_new'),
    
]