from django.urls import path
from . import views

urlpatterns  = [
    path('clients/<int:id>/',views.MesClient,name='clients'),
]