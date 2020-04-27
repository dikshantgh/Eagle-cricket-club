from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from cricket.models import Kheladi


class HomeListView(ListView):
    model = Kheladi
    template_name = 'cricket/home.html'


class PlayerDetailView(DetailView):
    model = Kheladi
    template_name = 'cricket/player_detail.html'
