from django.urls import path
from . import views

urlpatterns = [

    path('/<str:pk>', views.list_client, name='client',),  # la vue qui sera activée lorsque je suis dans l'accueil
    path('/', views.ajouter_client, name='ajouter_client',),
    path('/<str:pk>', views.modifier_client, name='modifier_client',),
    path('/<str:pk>', views.supprimer_client, name='supprimer_client',),
]
