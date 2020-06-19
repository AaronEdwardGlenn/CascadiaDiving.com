from django.shortcuts import render
from .forms import JoinDiveClubForm
from django.contrib.auth.decorators import login_required


@login_required
def join(request):
    j_form = JoinDiveClubForm(instance=request.user)
    context = {
        'join': 'active',
        'u_form': j_form

    }
    return render(request, 'join/join.html', context)
