from distutils.command.upload import upload
from importlib.resources import contents
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from users.models import Profile


class Image(models.Model):
    title = models.CharField(max_length=100, null=True )
    image = CloudinaryField('image', null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    # class Meta:
        
    #     ordering = ["-timestamp", "-updated"]

    def save_image(self):
        
        self.save()

    def delete_image(self):
       
        self.delete()
    @property
    def num_liked(self):
        return self.liked.all().count()

    @classmethod
    def update_caption(cls, self, caption):
        update_cap = cls.objects.filter(id = id).update(caption = caption)
        return update_cap

    def __str__(self):
        return self.image_name

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null = True)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10, null = True)

    def __str__(self):
        return self.image

class Subscribers(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments

    def __str__(self):
        return self.comment

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'