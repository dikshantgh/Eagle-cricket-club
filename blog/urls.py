# blog/urls.py
"""THis is the url route for app blog"""
from django.urls import path

from blog import views
app_name = 'blog'
urlpatterns = [
    path('blog-list/', views.BlogListView.as_view(), name='blog_list'),
    path('blog-detail/<slug:slug>/<uuid:uuid>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('update/<slug:slug>/<uuid:uuid>/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('tag/<slug:tag_slug>/', views.BlogByTagListView.as_view(), name='blog_list_tag'),
    path('search/', views.SearchResultListView.as_view(), name='search_result'),
]