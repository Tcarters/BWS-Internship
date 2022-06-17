#from django.shortcuts import render

# Create your views here.

#Use class based views
# from email import message
from django.contrib import messages

from django import forms
from django.views.generic import TemplateView, DetailView, FormView
# from requests import request
# from matplotlib.style import context

from .forms import PostForm

from .models import Post

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['my_thing'] = "Hello world :P this is dynamic"
        context['posts'] = Post.objects.all().order_by('-id')
        return context


class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm 
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        print("This was  valid !!!!")
        print(form.cleaned_data['text'])

        # Create a new Post
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, 'Your post was successfull ')
        return super().form_valid(form)