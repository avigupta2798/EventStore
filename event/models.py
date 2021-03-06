import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=250, null = True)
    content_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_liked = models.ManyToManyField(User, related_name='likes', blank=True)
    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
