from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import AuthenticationForm

# Create a form posts 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

# Create a for comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body')

# Create a form login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))