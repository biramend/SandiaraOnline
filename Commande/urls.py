from django.urls import path
from . import views

urlpatterns = [
    path('panier/',views.CreateCommande,name='panier'),
    path('commandes/',views.MesCommande,name='commandes'),
]