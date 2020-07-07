from django.urls import path
from .views import UpcomingPostListView, UpcomingPostDetailView, UpcomingPostCreateView

urlpatterns = [
    path('upcoming/', UpcomingPostListView.as_view(), name='upcoming'),
    path('upcomingform/', UpcomingPostCreateView.as_view(), name='upcoming-form'),
    path('post/<int:pk>/', UpcomingPostDetailView.as_view(), name='upcoming-detail')
]
