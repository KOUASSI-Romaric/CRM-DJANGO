from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='accueil'),  # la vue qui sera activée lorsque je suis dans l'accueil
    path('liste_produit', views.liste_produit, name='liste_produit'),
    path('<str:pk>', views.list_produit, name='produit', ),
    path('ajout_produit/', views.ajouter_produit, name='ajout_produit'),
    path('modifier_produit/<str:pk>', views.modifier_produit, name='modifier_produit'),
    path('supprimer_produit/<str:pk>', views.supprimer_produit, name='supprimer_produit'),
]
