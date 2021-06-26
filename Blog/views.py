from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from Profile.models import *
# Create your views here.
def blog_list(request):
    all_posts=blog.objects.all()
    page=request.GET.get('page',1)
    global comments
    paginator = Paginator(all_posts, 3)
    try:
        all_posts = paginator.page(page)
    except PageNotAnInteger:
        all_posts = paginator.page(1)
    except EmptyPage:
        all_posts = paginator.page(paginator.num_pages)
    return render(request,'blog/list.html',{'all_post':all_posts })
def blog_detail(request,pk):
    post_detail=blog.objects.get(pk=pk)
    global comments
    comments=comment.objects.filter(comment_blog=post_detail,comment_reply=None)
    user=request.user
    user_detail=userprofile.objects.get(usrename=user)
    photo=user_detail.userphoto
    if request.method == 'POST':
            form1=CommentForm(request.POST,request.FILES)
            com_id=request.POST.get('com_id')
            print(com_id)
            reply=None
            if com_id:
                    reply=comment.objects.get(id=com_id)
            if form1.is_valid():
                comment_save=form1.save(commit=False)
                comment_save.comment_author=user
                comment_save.comment_blog=post_detail
                comment_save.current_city=user_detail.city
                comment_save.author_email=user_detail.email
                comment_save.comment_reply=reply
                comment_save.save()
                return redirect('blog:list')
    else:
        form1=CommentForm()
    return render(request,'blog/detail.html',{'detail':post_detail,'form1':form1,'comments':comments,'photo':photo})
def like_post(request,pk):
    post_like=blog.objects.get(pk=pk)
    if request.user not in post_like.liked_post.all():
        post_like.liked_post.add(request.user)
    if request.user in post_like.disliked_post.all():
        post_like.disliked_post.remove(request.user)
    return redirect('blog:list') 
def dislike_post(request,pk):
    post_like=blog.objects.get(pk=pk)
    if request.user not in post_like.disliked_post.all():
        post_like.disliked_post.add(request.user)
    if request.user in post_like.liked_post.all():
        post_like.liked_post.remove(request.user)
    return redirect('blog:list')