from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, default="My Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null = True)
    date = models.DateField(auto_now_add=True)
    category = models.CharField( max_length=255, default="News")
        
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article', kwargs={"pk": self.id})

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
      return '%s - %s' % (self.post.title, self.name)

