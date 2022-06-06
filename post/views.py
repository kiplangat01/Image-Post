from django.shortcuts import render
from django.views.generic import ListView
from .models import Post



def home(request):
    context = {
        'posts' : Post.objects.all()
    }
     
    return render(request, 'post/home.html',  context)


class PostListView(ListView):
    model = Post
    template_name = 'post/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):
    return render(request, 'post/about.html')