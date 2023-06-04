from django import forms
from .models import Post, CommentPost


class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=('title','text',)



class CommentForm(forms.ModelForm):

    class Meta:
        model=CommentPost
        fields=('text',)
