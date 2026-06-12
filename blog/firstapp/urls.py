from django.urls import path
from . import views

urlpatterns= [
    path('html/',views.html_view, name='html_view'),
    path('home/',views.first_view, name='first_view'),
    path('profile/<int:id>',views.profile_view, name='profile_view'),
]