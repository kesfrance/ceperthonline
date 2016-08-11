from django import forms
from revportal.models import Post, UserProfile, Review
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'synopsis', 'tag', 'image']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['picture',]

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['content', 'post', ]