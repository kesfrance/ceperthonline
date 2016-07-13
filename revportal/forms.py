from django import forms
from revportal.models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'synopsis', 'tag', 'image']