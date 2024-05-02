from django.urls import path
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    path('',views.post_list,name='home'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
    # path("", views.Post_List.as_view(), name="posts"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',views.post_detail,name='post_detail'),
    # path('<int:year>/<int:month>/<int:day>/<slug:post>',views.Post_Detail.as_view(),name='post_detail'),
    path('comment/<int:post_id>',views.comment_post,name='comment_post'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/',views.post_list,name='search'),
    path('profile/<int:user_id>/',views.profile,name='profile'),
    path('delete/<int:comment_id>',views.delete_comment,name='delete'),
    path('like/<int:post_id>/',views.like_post,name='like'),
    path('settings/',views.settings,name='settings'),
    path('add_post/',views.add_post,name='add_post'),
    path('delete_post/<int:post_id>',views.delete_post,name='delete_post'),


    # path('update/<int:comment_id>',views.update_comment,name='update')
]
