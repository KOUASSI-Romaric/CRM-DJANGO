from django.shortcuts import render


# Create your views here.

def inscriptionPage(request):
    context = {}
    return render('compte/inscription.html', context)


def loginPage(request):
    context = {}
    return render('compte/login.html', context)
