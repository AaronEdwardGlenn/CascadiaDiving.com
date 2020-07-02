from django.urls import path
from .views import UpcommingDivesListView


urlpatterns = [
    path('upcomming/', UpcommingDivesListView.as_view(), name='upcomming-dives')
]
