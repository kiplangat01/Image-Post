from django.urls import path
from django.urls import include, re_path
from . import views 
from .views import PostListView, PostDetailView, PostCreateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostListView.as_view(), name='post-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('saveimage/', views.SaveImage),  
    path('about/', views.about, name='post-about'),
    path('like', views.like_post,name = 'like-post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
