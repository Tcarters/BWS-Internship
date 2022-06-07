#from django.shortcuts import render

# Create your views here.

#Use class based views

from django.views.generic import TemplateView
# from matplotlib.style import context


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_thing'] = "Hello world :P this is "
        return context