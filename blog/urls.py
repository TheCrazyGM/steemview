from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.trending, name='trending'),
    path('trending/', views.trending, name='trending'),
    path('hot/', views.hot, name='hot'),
    path('promoted/', views.promoted, name='promoted'),
    path('latest/', views.latest, name='latest'),
    re_path(r'^@(?P<author>[^~,]+)\/followers/?$', views.followers, name='followers'),
    re_path(r'^@(?P<author>[^~,]+)\/following/?$', views.followers, name='followers'),
    re_path(r'^@(?P<author>[^~,]+)\/(?P<permlink>[^~,]+/?$)', views.post_detail, name='post_detail'),
    re_path(r'^@(?P<author>[^~,]+/?$)', views.blog_posts, name='blog_posts'),
    re_path(r'^(?P<tag>[^~,]+)\/\@(?P<author>[^~,]+)/(?P<permlink>[^~,]+/?$)', views.post_detail, name='post_detail'),

    path('post/new/', views.post_new, name='post_new'),
    path('@<slug:author>/<slug:permlink>/edit/', views.post_edit, name='post_edit'),

]
