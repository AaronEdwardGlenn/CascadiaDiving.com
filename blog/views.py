from django.shortcuts import render
from .models import DivePost


def home(request):
    context = {
        'posts': DivePost.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def carousel(request):
    return render(request, 'blog/carousel.html')
