from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'post/home.html')

def about(request):
    return HttpResponse('<h1>Blog about</h1>')