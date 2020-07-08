from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, RecentDivesListView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-diveposts'),
    path('recent/', RecentDivesListView.as_view(), name='recent-dives'),
    path('about/', views.about, name='blog-about'),
    path('carousel/', views.carousel, name='blog-carousel'),
    path('spearfishing/', views.spearfishing, name='spearfishing'),
    path('lessons/', views.lessons, name='lessons'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
]
