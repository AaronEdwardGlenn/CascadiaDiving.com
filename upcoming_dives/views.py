from django.shortcuts import render
from .forms import UpcommingDivesForm
from django.contrib.auth.decorators import login_required
from .models import Upcoming_Dives
from django.views.generic import ListView, DetailView


@login_required
def upcoming(request):
    ud_form = UpcommingDivesForm()

    if ud_form.is_valid():
        ud_form.save()

    context = {
        'ud_form': ud_form
    }

    return render(request, 'upcoming_dives/upcoming_dives_form.html', context)


class UpcomingPostListView(ListView):
    model = Upcoming_Dives
    template_name = 'upcoming_dives/upcoming_dives.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 3


class UpcomingPostDetailView(DetailView):
    model = Upcoming_Dives
