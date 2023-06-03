from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

# Require login information before being able to create a post
@login_required
# Create a function to show the list of posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts':posts})

# Require login information before being able to create a post
@login_required
# Create a function to display create post attributes to the user
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    form = PostForm()
    return render(request, 'create_post.html', {'form':form})

# Create a function to display post and comments related to each post to the user
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post':post, 'comments':comments})

# Create a function that display the interface that allows the user to add comments to posts
def add_comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('add_comment')
    form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'post':post})

# Create a function that displays a registration screen to the user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Create a function that displays a login screen to the user
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        return render(request, 'registration/login.html', {'error_message': 'Invalid login credentials.'})
    return render(request, 'registration/login.html')

# Require login before logout
@login_required
# Create a function that displays a logout screen to the user
def user_logout(request):
    logout(request)
    return redirect('register')