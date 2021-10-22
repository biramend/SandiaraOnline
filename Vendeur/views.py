from django.shortcuts import render, HttpResponse
from .forms import VendeurForm
from .models import Vendeur


# Create your views here.
def MesVendeurs(request):
    vendeurs = Vendeur.objects.all()

    context = {'vendeurs': vendeurs}
    return render(request, 'vendeurs/index.html', context)


def CreateVendeur(request):
    # form = VendeurForm()
    if request.method == "POST":
        form = VendeurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form = VendeurForm()
    context = {'form': form}
    return render(request, 'vendeurs/create.html', context)