from django.shortcuts import render,HttpResponse
from .models import Client
from Commande.models import Commande
# Create your views here.
def MesClient(request,id):
    client = Client.objects.get(id=id)
    commande =client.commande_set.all()
    totol = commande.count()
    contex = {'client':client,'commande':commande,'total':totol}
    return render(request,'clients/list_client.html',contex)