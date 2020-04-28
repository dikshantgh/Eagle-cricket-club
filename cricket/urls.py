# cricket/urls.py
"""THis is the url route for app cricket"""
from django.urls import path
from django.views.generic import TemplateView

from cricket import views

app_name='cricket'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('player-detail/<slug:slug>/<uuid:uuid>/', views.PlayerDetailView.as_view(), name='player_detail'),
    path('player-update/<slug:slug>/<uuid:uuid>/', views.PlayerUpdateView.as_view(), name='player_update'),
    path('ground/', TemplateView.as_view(template_name='cricket/ground.html'), name='ground'),
]