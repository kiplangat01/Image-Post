from django.contrib import admin
from .models import Image, Comment, Subscribers, Like, Follow


admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Subscribers)
admin.site.register(Like)
admin.site.register(Follow)

