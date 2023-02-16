from django.shortcuts import render, redirect, HttpResponse
from .models import Client
from .forms import ClientForm


# Create your views here.
def list_client(request, pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()
    context = {'client': client, 'commande': commande, 'commande_total': commande_total}
    return render(request, 'client/list_client.html', context)


def ajouter_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'client/ajouter_client.html', context)


def modifier_client(request, pk):
    client = Client.objects.get(id=pk)

    return render(request, 'client/modifier_client.html')


def supprimer_client(request, pk):
    client = Client.objects.get(id=pk)

    return render(request, 'client/supprimer_client.html')
