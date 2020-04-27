# cricket/urls.py
"""THis is the url route for app cricket"""
from django.urls import path

from cricket import views

app_name='cricket'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('player-detail/<slug:slug>/<uuid:uuid>/', views.PlayerDetailView.as_view(), name='player_detail'),
]