from django.shortcuts import render

# Create your views here.
# blog/views.py
# from django.views.generic import ListView, DetailView
#
# from .models import Post
#
#
# class BlogListView(ListView):
#     model = Post
#     template_name = 'home.html'
#
#
# class BlogDetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'


from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
