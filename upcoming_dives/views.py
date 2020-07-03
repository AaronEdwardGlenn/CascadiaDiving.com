from django.shortcuts import render
from .forms import UpcommingDivesForm
from django.contrib.auth.decorators import login_required


@login_required
def upcoming(request):
    ud_form = UpcommingDivesForm()

    context = {
        'ud_form': ud_form
    }

    return render(request, 'upcoming_dives/upcoming_dives.html', context)


# Create your views here.
