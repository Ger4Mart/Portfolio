from django.urls import path
from . import views

#patterns for the urls
urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/', views.home, name="post"),
    path('profile/', views.profile, name ="profile"),
    path('test/', views.test, name='test'),
    
    
]