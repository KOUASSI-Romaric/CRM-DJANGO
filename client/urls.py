from django.urls import path
from . import views

urlpatterns = [

    path('<str:pk>', views.list_client, name='client'),  # la vue qui sera activée lorsque je suis dans l'accueil
    path('liste_client/', views.liste_client, name='liste_client'),
    path('ajout_client/', views.ajouter_client, name='ajout_client'),
    path('modifier_client/<str:pk>', views.modifier_client, name='modifier_client'),
    path('supprimer_client/<str:pk>', views.supprimer_client, name='supprimer_client'),
]
