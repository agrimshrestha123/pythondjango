from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first_view(request):
    return HttpResponse("Hello, World!! This is the first view.")

def profile_view(request, id):
    return HttpResponse(f"This is the profile view for user with ID: {id}")

def html_view(request):
    message= "welcome to the html view"
    return render(request, 'firstapp/index.html', { 'message': message })