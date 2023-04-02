from django.urls import path

from posts.views import PostsListView, LatestPostsView, PostDetailView

app_name = 'posts'

urlpatterns = [
    path('', LatestPostsView.as_view(), name='latest'),
    path('feed/', PostsListView.as_view(), name='feed'),
    path('<slug:slug>/', PostDetailView.as_view(), name='details'),
]
