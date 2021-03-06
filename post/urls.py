from django.urls import path
from . import views 
from .views import PostListView, PostDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostListView.as_view(), name='post-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('saveimage/', views.SaveImage),  
    path('about/', views.about, name='new-post'),
    path('like/<str:pk>', views.like,name = 'like-post'),
    path('comments/<str:pk>', views.comments, name='comments'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
