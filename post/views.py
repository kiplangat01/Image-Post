from turtle import title
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Image, User, Comment, Like
from .forms import ImageUploadForm, CommentForm
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    posts = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    # if request.method == "POST":
    #     form = ImageUploadForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         image = form.save(commit = False)
    #         image.user = request.user.profile
    #         image.save()
    #         messages.success(request, f'Your Picture Was succesfully Added!')
    #         return redirect('blog-home')
    # else:
        # form = ImageUploadForm()
    return render(request, 'post/home.html',  {'posts':posts})


class PostListView(ListView):
    model = Image
    template_name = 'post/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Image

class PostCreateView(CreateView):
    model = Image
    fields = ['title', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"post_detail.html", {"image":image})

def about(request):
    return render(request, 'post/about.html')

def like_post(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        img_obj = Image.objects.get(id = image_id)
        if user in img_obj.liked.all():
            img_obj.liked.remove(user)
        else:
            img_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user = user, image_id = image_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect(request, 'index.html')

@login_required 
def comment(request,image_id):
        current_user=request.user
        image = Image.objects.get(id=image_id)
        user_profile = User.objects.get(username=current_user.username)
        comments = Comment.objects.all()
        if request.method == 'POST':
                form = CommentForm(request.POST, request.FILES)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.image = image
                        comment.user = request.user
                        comment.save()  
                return redirect('index')
        else:
                form = CommentForm()
        return render(request, 'comment.html',locals())

@login_required
def SaveImage(request):
    print('post')
    if request.method == 'POST':
        print('text')
        # form = Image(request.POST, request.FILES)
        # if form.is_valid():
        author = request.user
        title = request.POST['title']
        image = request.FILES['image']
        image = Image(author = author, title = title, image=image)
        image.save()
                    
        return redirect('post-home')

    return render(request, 'post-home')