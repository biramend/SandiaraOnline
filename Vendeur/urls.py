from django.urls import path
from . import views

urlpatterns = [
    path('vendeurs/',views.MesVendeurs,name='vendeurs'),
    path('vendeurcreate/',views.CreateVendeur,name='vendeurcreate'),
]