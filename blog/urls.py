from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('carousel/', views.carousel, name='blog-carousel'),
    path('spearfishing/', views.spearfishing, name='spearfishing'),
    path('lessons/', views.lessons, name='lessons'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
]
