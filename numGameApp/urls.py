from django.urls import path
from . import views

urlpatterns = [
    path('', views.numIndex),
    path('numDash/', views.numDash),
    path('playerName/', views.addName),
]