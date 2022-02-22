from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from .models import Group, Post

User = get_user_model()


def index(request):
    template = "posts/index.html"
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "posts": posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = "posts/group_list.html"
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "group": group,
        "posts": posts,
    }
    return render(request, template, context)


def profile(request, username):
    template = "posts/profile.html"
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author__username=username)
    posts_count = Post.objects.filter(author__username=username).count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "posts_count": posts_count,
        "posts": posts,
        "user": user,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = "posts/post_detail.html"
    post = get_object_or_404(Post, id=post_id)
    posts_count = Post.objects.filter(author=post.author).count()
    context = {
        "posts_count": posts_count,
        "post": post,
    }
    return render(request, template, context)
