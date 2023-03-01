from django.shortcuts import render, HttpResponse, redirect
from commande.models import Commande
from client.models import Client
from .models import Produit, Tag
from .forms import ProduitForm
from .filtre import ProduitFiltre
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    produits = Produit.objects.all()
    myFilterProduit = ProduitFiltre(request.GET, queryset=produits)
    produits = myFilterProduit.qs
    context = {'commandes': commandes, 'clients': clients, 'produits': produits, 'myFilterProduit': myFilterProduit}
    return render(request, 'produit/accueil.html', context)


@login_required(login_url='login')
def liste_produit(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    produits = Produit.objects.all()
    myFilterProduit = ProduitFiltre(request.GET, queryset=produits)
    produits = myFilterProduit.qs
    context = {'commandes': commandes, 'clients': clients, 'produits': produits, 'myFilterProduit': myFilterProduit}
    return render(request, 'produit/liste_produit.html', context)


@login_required(login_url='login')
def list_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    commande = produit.commande_set.all()
    tag = produit.tag.all()
    commande_total = commande.count()
    context = {'produit': produit, 'commande': commande, 'commande_total': commande_total, 'tag': tag}
    return render(request, 'produit/list_produit.html', context)


@login_required(login_url='login')
def ajouter_produit(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'produit/ajouter_produit.html', context)


@login_required(login_url='login')
def modifier_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    form = ProduitForm(instance=produit)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'produit/ajouter_produit.html', context)


@login_required(login_url='login')
def supprimer_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('/')
    context = {'item': produit}
    return render(request, 'produit/supprimer_produit.html', context)
