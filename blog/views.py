from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import DivePost
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'posts': DivePost.objects.all(),
        'home': 'active'
    }
    return render(request, 'blog/home.html', context)


class RecentDivesListView(ListView):
    model = DivePost
    template_name = 'blog/recent_dives.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'recent': 'active'})
        return context


class UserPostListView(ListView):
    model = DivePost
    template_name = 'blog/user_diveposts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return DivePost.objects.filter(diver=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = DivePost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = DivePost
    fields = ['title', 'dive_site', 'content', 'image1', 'image2', 'image3']

    def form_valid(self, form):
        form.instance.diver = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'log': 'active'})
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DivePost
    fields = ['title', 'dive_site', 'content', 'image1', 'image2', 'image3']

    def form_valid(self, form):
        form.instance.diver = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.diver:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DivePost
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.diver:
            return True
        return False


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


def naturalist(request):
    context = {
        'naturalist': 'active'
    }
    return render(request, 'blog/naturalist.html', context)


def pnwdive(request):
    context = {
        'pnwdive': 'active'
    }
    return render(request, 'blog/pnw_diving.html', context)
