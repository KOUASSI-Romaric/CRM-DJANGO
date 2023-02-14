from django.urls import path
from . import views

urlpatterns = [

    path('/<str:pk>', views.list_client, name='client',),  # la vue qui sera activée lorsque je suis dans l'accueil
]
