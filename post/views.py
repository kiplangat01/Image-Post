from django.shortcuts import render
from .models import Post




def home(request):
    context = {
        'post' : Post.objects.all()
    }
     
    return render(request, 'post/home.html')

def about(request):
    return render(request, 'post/about.html')