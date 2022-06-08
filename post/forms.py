from django import forms
from .models import Image, Comment



class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image' ]

    def form_valid(self, form):
        form.instance.user = self.request.profile
        return super().form_valid(form)

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image','user']

    class Meta:
        model = Comment
        fields = ('comment',)
