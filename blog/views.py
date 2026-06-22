from django.shortcuts import render
from .models import post

# Create your views here.
def post_list(request):
    all_posts = post.objects.all()

    context = {
        'posts' : all_posts
    }
    return render(request,'blog/post_list.html',context)