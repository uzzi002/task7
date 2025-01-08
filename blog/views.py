from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()

    # Convert all post titles to uppercase
    for post in posts:
        post.title = post.title.upper()

    return render(request, 'blog/post_list.html', {'posts': posts})