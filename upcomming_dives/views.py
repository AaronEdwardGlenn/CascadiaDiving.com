from django.views.generic import ListView
from .models import UpcommingDivePost


class UpcommingivesListView(ListView):
    model = UpcommingDivePost
    template_name = 'upcomming_dives/upcomming.html'
