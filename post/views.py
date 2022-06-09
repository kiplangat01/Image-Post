from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Image, User, Comment, Like
from .forms import ImageUploadForm, CommentForm
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    posts = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'post/home.html',  {'posts':posts})


class PostListView(ListView):
    model = Image
    template_name = 'post/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Image

def about(request):
    return render(request, 'post/new_post.html')

def like(request, pk):
    user = request.user
    image = Image.objects.get(id=pk)
    current_likes = image.likes
    liked = Like.objects.filter(user=user, image=image).count()

    if not liked:
            class_name = 'red'
            like = Like.objects.create(user=user, image=image)
            current_likes = current_likes + 1

    else:
            Like.objects.filter(user=user, image=image).delete()
            current_likes = current_likes - 1

    image.likes = current_likes
    image.save()

    return HttpResponseRedirect(reverse('post-home'))

@login_required(login_url='')
def comments(request, pk):
    image = Image.objects.get(id=pk)
    comments = Comment.objects.filter(image=image)

    if request.method == 'POST':
        comment = request.POST.get('comment')
        print(comment)
        comment_owner = User.objects.get(username=request.user)
        new_comment = Comment.objects.create(
            comment=comment, image=image, user=comment_owner)
        new_comment.save()

    context = {'comment': comments, 'image': image}
    return render(request, 'post/comments.html', context)

@login_required
def SaveImage(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        image = request.FILES['image']
        image = Image(author = author , title = title, image=image )
        image.save()
        return redirect('post-home')

    return render(request, 'new-post')