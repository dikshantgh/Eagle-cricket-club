# cricket/urls.py
"""THis is the url route for app cricket"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path
from django.views.generic import TemplateView

from cricket import views

app_name='cricket'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('player-detail/<slug:slug>/<uuid:uuid>/', views.PlayerDetailView.as_view(), name='player_detail'),
    path('player-update/<slug:slug>/<uuid:uuid>/', views.PlayerUpdateView.as_view(), name='player_update'),
    # path('ground/', login_required(TemplateView.as_view(template_name='cricket/ground.html')), name='ground'),
    path('ground/', TemplateView.as_view(template_name='cricket/ground.html'), name='ground'),
    path('game/', TemplateView.as_view(template_name='cricket/game.html'), name='game'),
    path('gang/', views.GangShareCreateView.as_view(), name='gang_share'),
]