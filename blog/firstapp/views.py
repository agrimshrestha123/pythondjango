from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Posts
from .forms import CreateBlogPostForm

# Create your views here.
def first_view(request):
    return HttpResponse("Hello, World!! This is the first view.")

def profile_view(request):
    message="my profile picture"
    return render(request, "firstapp/profile.html", {"message":message})

def html_view(request):
    message= "welcome to the html view"
    return render(request, 'firstapp/index.html', { 'message': message })

def create_post(request):
    # CRUD operation
    if request.method=='POST':
        post=CreateBlogPostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('html_view')
    else:
        post=CreateBlogPostForm()

    return render(request, "firstapp/create_post.html",{"post":post})

from .models import Posts
def get_post_view(request):
     posts=Posts.objects.all()
     error_message ="something went wrong."
     return render(request, "firstapp/all_post.html", {"posts": posts,"error_message" : error_message})