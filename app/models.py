from django.db import models

from .managers import PublishedManager
from django.utils import timezone
from django.urls import reverse_lazy
from taggit.managers import TaggableManager
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.



class CustomUser(AbstractUser):
    bio=models.TextField(blank=True)
    photo=models.ImageField(upload_to='user-images/',blank=True,null=True)
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT='DF','Draft'
        PUBLISHED='PB','Published'
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='blog_posts')
    tags=TaggableManager()
    title=models.CharField(max_length=200)
    body=RichTextField()
    image=models.ImageField(upload_to='post-images/',blank=True,null=True)
    publish=models.DateTimeField(default=timezone.now)
    slug=models.SlugField(max_length=200,unique_for_date='publish')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    likes=models.ManyToManyField(CustomUser,related_name='likes')
    ###
    objects=models.Manager() #default manager
    published=PublishedManager() #custom manager

    ###
    class  Meta:
        ordering=['-publish']
        indexes=[
        models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse_lazy("post_detail", kwargs={
        "year": self.publish.year,
        'month':self.publish.month,
        'day':self.publish.day,
        'post':self.slug
        }) # post_detail is url pattern name
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(CustomUser,on_delete=models.PROTECT)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


    def __str__(self):
        return f' comment by {self.user} on {self.post.title}'
    class meta:
        ordering=['created']
        indexes=[models.Index(fields=['created'])]