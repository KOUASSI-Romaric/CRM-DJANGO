from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreerUtilisateur


# Create your views here.

def inscription_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Compte créé avec succès pour '+user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'compte/inscription.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.info(request, "Il y a une erreur! Veillez recommencer")
    context = {}
    return render(request, 'compte/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
