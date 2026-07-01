from django.urls import path
from . import views

urlpatterns= [
    path('',views.html_view, name='html_view'),
    path('home/',views.first_view, name='first_view'),
    path('profile/',views.profile_view, name='profile_view'),
    path('create_post/',views.create_post,name='create_post'),
    path('all_post/',views.get_post_view,name='all_post'),
    path('post/<int:post_id>',views.post_detail_view,name="post_detail"),
    path('signup/',views.signup_view, name='signup'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout')


]