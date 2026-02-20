from django import forms
from .models import Blog,BlogPost
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'description']
        labels = {
            'name': 'Blog name',
            'description': 'Description',
        }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}