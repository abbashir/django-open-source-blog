from django.contrib import admin
from django.urls import path
from .import views

app_name = 'posts'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('post/<slug:slug>', views.post_details, name='post_details'),
    path('category/<slug:slug>', views.category_wise_post,
         name='category_wise_post'),
    path('post/create', views.post_create, name='post_create'),
    path('search/', views.blog_search, name='blog_search'),
]
