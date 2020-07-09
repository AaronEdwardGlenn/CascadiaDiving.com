from django.shortcuts import render
from .forms import UpcommingDivesForm
from django.contrib.auth.decorators import login_required
from .models import Upcoming_Dives
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# @login_required
# def upcoming(request):
#     ud_form = UpcommingDivesForm()
#
#     if ud_form.is_valid():
#         ud_form.save()
#
#     context = {
#         'ud_form': ud_form
#     }
#
#     return render(request, 'upcoming_dives/upcoming_dives_form.html', context)

def checklist(request):
    return render(request, 'upcoming_dives/trip_info.html')


class UpcomingPostCreateView(LoginRequiredMixin, CreateView):
    model = Upcoming_Dives
    fields = ['title', 'date', 'location', 'content', 'image']

    def form_valid(self, form):
        return super().form_valid(form)


class UpcomingPostListView(ListView):
    model = Upcoming_Dives
    template_name = 'upcoming_dives/upcoming_dives.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'upcoming': 'active'})
        return context


class UpcomingPostDetailView(DetailView):
    model = Upcoming_Dives
