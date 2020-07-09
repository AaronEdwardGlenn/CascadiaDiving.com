from django.shortcuts import render


def join(request):
    context = {
        'join': 'active',

    }
    return render(request, 'join/join.html', context)
