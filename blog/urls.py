from django.urls import path  

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserProfilePostListView, about

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='home-page'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('post/list/<username>/', UserProfilePostListView.as_view(), name='mark-user-home-page'),

    path('about/', about, name='about-page')
]