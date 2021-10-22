from django.shortcuts import render,HttpResponse,redirect
from .models import Produit,Categorie,Vendeur
from .forms import ProduitForm
# Create your views here.
def MesProduit(request):
    produits = Produit.objects.order_by('price')[:4]
    produits1 = Produit.objects.order_by('price')[5:]
    categories = Categorie.objects.all()
    context = {'produits':produits,'categories':categories,'produits1':produits1}
    return render(request,'produits/index.html',context)


def CreateProduit(request):
    categories = Categorie.objects.all()
    form = ProduitForm()
    if request.method=="POST":
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ProduitForm()
    context = {'form':form,'categories':categories}
    return render(request,'produits/create.html',context)

def editProduit(request,id):
    categories = Categorie.objects.all()
    vendeurs = Vendeur.objects.all()
    produit = Produit.objects.get(id=id)
    context = {'produit':produit,'categories':categories,'vendeurs':vendeurs}
    return render(request,'produits/edit.html',context)


def updateProduit(request,id):
        categories = Categorie.objects.all()
        vendeurs = Vendeur.objects.all()
        produit = Produit.objects.get(id=id)
        form = ProduitForm(request.POST,instance=produit)
        if request.method=="POST":
            form = ProduitForm(request.POST,instance=produit)
            if form.is_valid():
                form.save()
                return redirect('/')

        form = ProduitForm()
        context = {'produit': produit, 'categories': categories, 'vendeurs': vendeurs,'form':form}
        return render(request,'produits/edit.html',context)



def MesCategories(request,id):
    categories = Categorie.objects.all()
    cats=Categorie.objects.get(id=id)
    produits = Produit.objects.filter(categorie=id)[:2]
    produits1 = Produit.objects.filter(categorie=id)[2:]
    context={'categories':categories,'produits':produits,'cats':cats,'produits1':produits1}
    return render(request,'categories/mescategories.html',context)


def showProduit(request,id):

    categories=Categorie.objects.all()
    produit = Produit.objects.get(id=id)
    # prodts = Produit.objects.filter(categorie=id)[:8]
    context={'categories':categories,'produit':produit}
    return render(request,'produits/show.html',context)

def menu(request):
    produits = Produit.objects.order_by('price')[:4]
    produits1 = Produit.objects.order_by('price')[5:]
    categories = Categorie.objects.all()
    context = {'produits':produits,'categories':categories,'produits1':produits1}
    return render(request,'base/menu.html',context)


def search_view(request):
    query = request.GET["article"]
    list_articles = Produit.objects.filter(name__icontains=query)
    context = {'list_articles':list_articles}
    return render(request,'produits/search.html',context)