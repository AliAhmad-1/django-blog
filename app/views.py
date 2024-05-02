from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Post,Comment,CustomUser
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView,DetailView,DeleteView
from .forms import EmailPostForm,CommentForm,SearchForm,PostForm
from django.core.mail import send_mail
from django.contrib import messages
from taggit.models import Tag
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.urls import reverse
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from django.contrib.auth.decorators import login_required
# fcbv posts-list


def post_list(request,tag_slug=None):
    posts_list=Post.published.all()
    tags=Tag.objects.all()
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        posts_list=posts_list.filter(tags__in=[tag])
    paginator=Paginator(posts_list,3)
    page_number=request.GET.get('page',1)
    page_obj=paginator.get_page(page_number)
    form=SearchForm()
    query=None
    results=[]
    if 'query' in request.GET:
        form=SearchForm(request.GET)
        if form.is_valid():
            query=form.cleaned_data.get('query')
            searchvector=SearchVector('title','body')
            searchquery=SearchQuery(query)
            results=Post.objects.annotate(search=searchvector,rank=SearchRank(searchvector,searchquery)).filter(search=searchquery).order_by('-rank')
            page_obj=None
    return render(request,'home.html',context={'posts':page_obj,'tags':tags,'results':results,'searchform':form,'query':query})
# fbv post detail


@login_required
def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,status=Post.Status.PUBLISHED,
    slug=post,
    publish__year=year,
    publish__month=month,
    publish__day=day
    )
    id_tags=post.tags.values_list('id',flat=True)

    similar_posts=Post.published.filter(tags__in=id_tags).exclude(id=post.id).annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

    if request.method=='POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            to=form.cleaned_data.get('to')
            comment=form.cleaned_data.get('comment')
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{name} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
            f"{name}\'s comments: {comment}"
            send_mail(subject, message, 'eng.alihasanahmad@gmail.com',[to])
            messages.add_message(request,messages.SUCCESS,'The post has been shared successfully')
            return HttpResponseRedirect('/')
            
    else:
        form=EmailPostForm()

    commentform=CommentForm(request.POST)
    like=False
    if post.likes.filter(username=request.user):
        like=True


    context_data={
    'post_detail':post,
    'shareform':form,
    'form':commentform,
    'comments':post.comments.all(),
    'similar_posts':similar_posts,
    'like':like
  
    }

    return render(request,'detail.html',context=context_data)




# we can use this decoritor instead of :  (if request.method=='POST':)
    # @require_POST
def comment_post(request,post_id):
    
    post=get_object_or_404(Post,id=post_id)
    url_redirect=f'/{post.publish.year}/{post.publish.month}/{post.publish.day}/{post.slug}'
    user=request.user
    if request.method=='POST':
        form=CommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.user=user
            comment.save()
            return HttpResponseRedirect(url_redirect)
    else:
        form=CommentForm()
    return render(request,'detail.html',{'form':form})
def profile(request,user_id):
    if user_id:
        user=CustomUser.objects.get(id=user_id)
        posts=Post.published.filter(author=user)

    return render(request,'profile.html',{'posts':posts,'user':user})

def delete_comment(request,comment_id):
    comment=Comment.objects.get(id=comment_id)
    post=Post.objects.get(comments=comment)
    url_redirect=f'/{post.publish.year}/{post.publish.month}/{post.publish.day}/{post.slug}'
    comment.delete()
    return HttpResponseRedirect(url_redirect)
def like_post(request,post_id):
    post=Post.objects.get(id=post_id)
    post.likes.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())
def settings(request):
    user=request.user
    published_posts=Post.published.filter(author=user)
    draft_posts=Post.objects.filter(author=user,status=Post.Status.DRAFT)

    return render(request,'settings.html',context={'posts_published':published_posts,'draft_posts':draft_posts})

@login_required
def add_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)



        if form.is_valid():
            
            post=form.save(commit=False)
            tags=form.cleaned_data.get('tags')
            post.author=request.user
            if 'publish_post' in request.POST:
                post.status=Post.Status.PUBLISHED
                post.save()
            else:
                post.save()
            for tag in tags:
                post.tags.add(tag)
            return HttpResponseRedirect('/')
    else:
        form=PostForm()

    return render(request,'add_post.html',{'form':form})


def delete_post(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    post.delete()
    return HttpResponseRedirect('/settings')




# def update_comment(requset,comment_id):
#     comment=Comment.objects.get(id=comment_id)
#     post=Post.objects.get(comments=comment)
#     url_redirect=f'/{post.publish.year}/{post.publish.month}/{post.publish.day}/{post.slug}'
#     if request.method==POST:
#         form=CommentForm(request.POST,instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(url_redirect)
#     return render(request,'detail.html',{'updateform':form})


# GCBV post detail
# class Post_Detail(DetailView):
#     model=Post
#     template_name='detail.html'
#     context_object_name='post_detail'
#     def get_object(self):
#         year=self.kwargs.get('year')
#         month=self.kwargs.get('month')
#         day=self.kwargs.get('day')
#         slug=self.kwargs.get('post')
#         post = get_object_or_404(Post, publish__year=year, publish__month=month, publish__day=day, slug=slug)           
#         return post



# gcbv posts-list
# class Post_List(ListView):
#     model=Post
#     template_name='home.html'
#     context_object_name='posts'
#     def get_queryset(self):
#         queryset= super().get_queryset()
#         paginator=Paginator(queryset,2)
#         page_number=self.request.GET.get('page',1)
#         try:
#             page_obj=paginator.get_page(page_number)
#         except PageNotAnInteger:
#             page_obj=paginator.get_page(1)
#         return page_obj