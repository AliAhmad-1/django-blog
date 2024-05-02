from django.db import models

class PublishedManager(models.Manager):
    
    def get_queryset(self):
        from .models import Post
        queryset = super().get_queryset()
        queryset = queryset.filter(status=Post.Status.PUBLISHED)
        return queryset

