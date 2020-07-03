from django.urls import path
from .views import UpcomingPostListView

urlpatterns = [
    path('upcomingform/', UpcomingPostListView.as_view(), name='upcoming-form')
]
