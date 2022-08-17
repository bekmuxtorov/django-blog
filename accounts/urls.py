from django.urls import path,include
from . import views

urlpatterns = [
    path('edit/', views.BlogEditUserView, name='edit_profile'),
    path('account/', views.UserDatasView.as_view(), name="user_data"),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup')
]