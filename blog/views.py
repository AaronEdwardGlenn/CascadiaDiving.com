from django.shortcuts import render
from .models import DivePost
from django.views.generic import ListView


def home(request):
    context = {
        'posts': DivePost.objects.all(),
        'home': 'active'
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = DivePost
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


def about(request):
    context = {
        'about': 'active'
    }
    return render(request, 'blog/about.html', context)


def carousel(request):
    context = {
        'blog-home': 'active'
    }
    return render(request, 'blog/carousel.html', context)


def spearfishing(request):
    context = {
        'spearfishing': 'active'
    }
    return render(request, 'blog/spearfishing.html', context)


def lessons(request):
    context = {
        'lessons': 'active'
    }
    return render(request, 'blog/lessons.html', context)
