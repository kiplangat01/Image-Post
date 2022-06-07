from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include

urlpatterns=[
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow')
    ]