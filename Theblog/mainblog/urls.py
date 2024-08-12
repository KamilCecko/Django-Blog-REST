from django.urls import path
from . views import *


urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryView.as_view(), name='category-detail'),
    path('post/<int:pk>/comment/', PostCommentListView.as_view(), name='post-comments-list'),
    path('post/comment/<int:pk>/', CommentDetailView.as_view(), name='post-comment'),
]
