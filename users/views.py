from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    
   
        
    return render(request, 'users/register.html', )
