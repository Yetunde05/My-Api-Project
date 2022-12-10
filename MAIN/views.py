from django.shortcuts import render
from.models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "MAIN/home.html", context)


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {"post": post}
    return render(request, "MAIN/detail.html", context)
 