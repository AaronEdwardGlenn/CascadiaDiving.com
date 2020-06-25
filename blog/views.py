from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DivePost
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView
)


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


class PostDetailView(DetailView):
    model = DivePost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = DivePost
    fields = ['dive_site', 'content']

    def form_valid(self, form):
        form.instance.diver = self.request.user
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = DivePost
    fields = ['dive_site', 'content']

    def form_valid(self, form):
        form.instance.diver = self.request.user
        return super().form_valid(form)


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
