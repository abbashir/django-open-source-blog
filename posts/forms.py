from django import forms
from .models import Post


class postCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            'title',
            'content',
            'category',
            'author',
            'slug',
            'image',
        }
