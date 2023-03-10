from django.shortcuts import render
from app.models import Post, Tag, Comments
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm,SubscribeForm

# Create your views here.


def index(request):
    posts = Post.objects.all()
    subscribe_form = SubscribeForm()
    subscribe_success = None
    top_posts = Post.objects.all().order_by('-view_count')[0:3]
    recent_posts = Post.objects.all().order_by('-last_updated')[0:3]
    featured_post = Post.objects.filter(is_featured = True)
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            subscribe_success = 'Subscribed Succesfully'
            subscribe_form = SubscribeForm()
            # if subscribe_success:
            # return HttpResponseRedirect(reverse('home'))


    context = {'posts': posts, 'top_posts': top_posts,
               'recent_posts': recent_posts,
               'featured_post':featured_post,
               'subscribe_form':subscribe_form,
               'subscribe_success':subscribe_success
               }
    return render(request, 'app/index.html', context)


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comments.objects.filter(post=post, parent=None)
    form = CommentForm()
    parent_obj = None

    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            # check if it is a reply
            if request.POST.get('parent'):
                parent = request.POST.get('parent')
                parent_obj = Comments.objects.get(id=parent)
                if parent_obj:
                    comment_reply = comment_form.save(commit=False)
                    comment_reply.parent = parent_obj
                    comment_reply.post = post
                    comment_reply.save()
                    return HttpResponseRedirect(reverse('post_page', kwargs={'slug': slug}))
            else:
                comment = comment_form.save(commit=False)
                postId = request.POST.get("post_id")
                post = Post.objects.get(id=postId)
                comment.post = post
                comment.save()
                return HttpResponseRedirect(reverse('post_page', kwargs={'slug': slug}))

    if post.view_count is None:
        post.view_count = 1
    else:
        post.view_count = post.view_count + 1
    post.save()

    context = {
        "post": post,
        'form': form,
        'comments': comments
    }

    return render(request, 'app/post.html', context)


def tag_page(request, slug):
    top_posts = Post.objects.all().order_by('-view_count')[0:3]
    tags = Tag.objects.get(slug=slug)
    tag_posts = Post.objects.filter(tag=tags)
    context = {'tag': tags,
               'tag_posts':tag_posts,
               'top_posts':top_posts
               }
    return render(request, 'app/tag.html', context)
