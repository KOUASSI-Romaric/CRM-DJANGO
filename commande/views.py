from django.shortcuts import render, HttpResponse, redirect
from .forms import CommandeForm
from .models import Commande
from client.models import Client
from produit.models import Produit
from .filtre import CommandeFiltre


# Create your views here.
def list_commande(request):
    commande = Commande.objects.all()
    myFilterCommande = CommandeFiltre(request.GET, queryset=commande)
    commande = myFilterCommande.qs
    context = {'commande': commande, 'myFilterCommande': myFilterCommande}
    return render(request, 'commande/list_commande.html', context)


def ajouter_commande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'commande/ajouter_commande.html', context)


def modifier_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    form = CommandeForm(instance=commande)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)


def supprimer_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')
    context = {'item': commande}
    return render(request, 'commande/supprimer_commande.html', context)
