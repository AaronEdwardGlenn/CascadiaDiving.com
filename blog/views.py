from django.shortcuts import render
from .models import DivePost
dives = [
    {
        'site': 'Leafy Greans',
        'divers': 'Aaron Glenn',
        'date_dove': 'May 20, 2020',
        'content': 'awesome training site'
    },
    {
        'site': 'Dougan Falls',
        'divers': 'Aaron Glenn',
        'date_dove': 'June 2, 2020',
        'content': 'crazy waterfall'
    }
]


def home(request):
    context = {
        'posts': DivePost.objects.all(),
        'title': 'home'

    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

# Create your views here.
