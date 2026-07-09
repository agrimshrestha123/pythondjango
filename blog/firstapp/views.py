from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Posts
from .forms import CreateBlogPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# def first_view(request):
#     return HttpResponse("Hello, World!! This is the first view.")
@login_required
def profile_view(request):
    message="my profile picture"
    return render(request, "firstapp/profile.html", {"message":message})

@login_required
def html_view(request):
    posts=Posts.objects.all()
    user=request.user
    return render(request, 'firstapp/index.html', { "posts": posts, "user":user })

@login_required
def create_post(request):
    # CRUD operation
    if request.method=='POST':
        post=CreateBlogPostForm(request.POST)
        if post.is_valid():
            post.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('html_view')
    else:
        post=CreateBlogPostForm()

    return render(request, "firstapp/create_post.html",{"post":post})

from .models import Posts
@login_required
def get_post_view(request):
     posts=Posts.objects.all()
     error_message ="something went wrong."
     return render(request, "firstapp/all_post.html", {"posts": posts,"error_message" : error_message})

from django.shortcuts import get_object_or_404
def post_detail_view(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    return render(request, "firstapp/post_detail.html", {"post":post})

from .forms import SignUpForm
from django.contrib.auth.models import User       
from django.contrib.auth import login         

def signup_view(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            user=User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('html_view')
    else:
        form=SignUpForm()

    return render(request,'firstapp/signup.html',{"form":form})

from django.contrib.auth import authenticate,logout
def login_view(request):
    error=None
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(request, username=username, password= password)

        if user:
            login(request, user)
            return redirect('html_view')
        else:
            error = "Invalid username or password."

    
    return render(request, 'firstapp/login.html', {"error": error})


def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("login")
    
from django.shortcuts import get_object_or_404
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id) #, author=request.user

    if request.method == "POST":
        form = CreateBlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CreateBlogPostForm(instance=post)

    return render(request, "firstapp/edit_post.html", {
        "post": post,
        "form": form,
    })

from django.db.models import Q
def search(request):
    q=request.GET.get("q","").strip()
    results=Posts.objects.filter(Q(title__icontains=q)|Q(content__icontains=q))
    return render(request, 'firstapp/search_results.html', {"results":results,"query":q})