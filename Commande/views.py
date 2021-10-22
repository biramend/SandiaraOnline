from django.shortcuts import render,redirect
from Client.models import Client
from .models import Commande
from .forms import CommandeForm

# Create your views here.
def MesCommande(request):
    clients = Client.objects.all()
    commandes = Commande.objects.all()
    contex = {'clients': clients, 'commandes': commandes}
    return render(request, 'commandes/list_commande.html', contex)


def CreateCommande(request):
    form = CommandeForm()
    if request.method=="POST":
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('confirmation')
    form = CommandeForm()
    context = {'form':form}
    return render(request,'commandes/panier.html',context)