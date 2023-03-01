from django.shortcuts import render, redirect, HttpResponse
from .models import Client
from .forms import ClientForm
from commande.filtre import CommandeFiltre
from client.filtre import ClientFiltre
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def list_client(request, pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()
    myFilter = CommandeFiltre(request.GET, queryset=commande)
    commande = myFilter.qs
    context = {'client': client, 'commande': commande, 'commande_total': commande_total, 'myFilter': myFilter}
    return render(request, 'client/list_client.html', context)


@login_required(login_url='login')
def liste_client(request):
    client = Client.objects.all()
    myFilterClient = ClientFiltre(request.GET, queryset=client)
    client = myFilterClient.qs
    context = {'client': client, 'myFilterClient': myFilterClient}
    return render(request, 'client/liste_client.html', context)


@login_required(login_url='login')
def ajouter_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'client/ajouter_client.html', context)


@login_required(login_url='login')
def modifier_client(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'client/ajouter_client.html', context)


@login_required(login_url='login')
def supprimer_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/')
    context = {'item': client}
    return render(request, 'client/supprimer_client.html', context)
