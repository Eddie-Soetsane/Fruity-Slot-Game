from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.play_game, name='play_game'),
    path('play/', views.play, name='play'),
]
