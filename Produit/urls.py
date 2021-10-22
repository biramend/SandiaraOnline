from django.urls import path
from . import views

urlpatterns = [
    path('',views.MesProduit,name='accueil'),
    path('create/',views.CreateProduit,name='create'),
    path('menu/',views.menu,name='menu'),
    path('search/',views.search_view,name='search'),
    path('edit/<int:id>/', views.editProduit, name='edit'),
    path('update/<int:id>/', views.updateProduit),
    path('mescategories/<int:id>/', views.MesCategories,name='mescategories'),
    path('show/<int:id>/', views.showProduit,name='show'),


]