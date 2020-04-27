from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from cricket.forms import PlayerForm
from cricket.models import Kheladi


class HomeListView(ListView):
    model = Kheladi
    template_name = 'cricket/home.html'


class PlayerDetailView(LoginRequiredMixin, DetailView):
    model = Kheladi
    template_name = 'cricket/player_detail.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = str(self.request.user).lower()
        context['updating_user'] = str(get_object_or_404(Kheladi, uuid=self.kwargs['uuid'])).lower()
        return context


class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    model = Kheladi
    template_name = 'cricket/player_update.html'
    form_class = PlayerForm

    def dispatch(self, request, *args, **kwargs):
        current_user = str(self.request.user)
        updating_user = str(get_object_or_404(Kheladi, uuid=self.kwargs['uuid']))
        if current_user.lower() == updating_user.lower():
            return super(PlayerUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

