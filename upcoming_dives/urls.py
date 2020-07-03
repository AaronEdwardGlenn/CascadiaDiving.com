from django.urls import path
from .views import UpcomingPostListView, UpcomingPostDetailView
from . import views

urlpatterns = [
    path('upcoming/', UpcomingPostListView.as_view(), name='upcoming'),
    path('upcomingform/', views.upcoming, name='upcoming-form'),
    path('post/<int:pk>/', UpcomingPostDetailView.as_view(), name='upcoming-detail')
]
