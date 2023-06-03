from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create a model for the post database
class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# Create a model for the comment database
class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
