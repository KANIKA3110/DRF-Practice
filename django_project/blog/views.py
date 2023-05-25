from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
posts= [
    {
      'author':'CoreyMs',
      'title': 'blog post1',
      'content': 'first post content',
      'date-posted': 'Aug 27, 2018'  
    },
    
      {
      'author':'Jane Doe',
      'title': 'blog post2',
      'content': 'second post content',
      'date-posted': 'Aug 28, 2018'  
    },
]

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    context={
        'posts':posts    
        #'posts': Post.objects.all()
        }
    return render(request,'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html',{'title': 'About1'})
 
def home2(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    context={
        #'posts':posts    
        'posts': Post.objects.all()
        }
    return render(request,'blog/home2.html', context)

class PostListView(ListView):
    model= Post
    template_name='blog/home2.html'
    #<app> / <model> _ <viewtype> . html
    context_object_name='posts'
    ordering=['-date_posted'] #date_posted will give oldest to newest


class PostDetailView(DetailView):
    model= Post
   
class PostCreateView(CreateView) :
    model=Post
    fields=['title', 'content']
    
    def form_valid(self,  form):
      form.instance.author=self.request.user
      return super().form_valid(form)
  
class PostUpdateView(UpdateView) :
    model=Post
    fields=['title', 'content']
    
    def form_valid(self,  form):
      form.instance.author=self.request.user
      return super().form_valid(form)

class PostDeleteView( DeleteView):
    model= Post
    success_url='/blog/home2'
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
            
def about2(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about2.html',{'title': 'About2'})
 