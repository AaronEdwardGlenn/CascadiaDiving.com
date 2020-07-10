from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, RecentDivesListView


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-diveposts'),
    path('recent/', RecentDivesListView.as_view(), name='recent-dives'),
    path('about/', views.about, name='blog-about'),
    path('carousel/', views.carousel, name='blog-carousel'),
    path('spearfishing/', views.spearfishing, name='spearfishing'),
    path('naturalist/', views.naturalist, name='naturalist'),
    path('pnwdiving/', views.pnwdive, name='pnwdive'),
    path('recgear/', views.recgear, name='recgear'),
    path('lessons/', views.lessons, name='lessons'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
]
