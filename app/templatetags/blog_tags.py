from django import template
from django.db.models import Count
from ..models import Post
register=template.Library()

@register.simple_tag(name='my_tag_total_posts')
def total_posts():
    return Post.published.count()



@register.simple_tag(name='latest_posts')
def show_latest_posts(count=3):
    latest_posts = Post.published.order_by('-publish')[:count]
    return latest_posts


@register.simple_tag
def get_most_commented_posts(count=3):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]