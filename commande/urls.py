from django.urls import path
from . import views

urlpatterns = [

    path('list_commande/', views.list_commande, name='list_commande'),  # la vue qui sera activée lorsque je suis dans l'accueil
    path('ajout_commande/', views.ajouter_commande, name='ajout_commande'),
    path('modifier_commande/<str:pk>', views.modifier_commande, name='modifier_commande'),
    path('supprimer_commande/<str:pk>', views.supprimer_commande, name='supprimer_commande'),
]
