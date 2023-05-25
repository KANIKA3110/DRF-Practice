from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView, 
    PostDeleteView
)

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name='blog-about'),
    #path('home2/', views.home2, name="blog-home2"),
    path('about2/', views.about2, name='blog-about2'),
    path('home2/', PostListView.as_view(), name="blog-home2"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),

]