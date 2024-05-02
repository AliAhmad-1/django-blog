from django.contrib import admin
from .models import Post,Comment,CustomUser

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['pk','title','slug','body','publish','created','updated','status','image']

    list_filter=['author','publish','created','status']  
    search_fields=['title','body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['user','post','body','created','updated','active']
    

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=['username','email','bio','photo']
    
