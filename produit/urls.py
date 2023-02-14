from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='accueil'),  # la vue qui sera activée lorsque je suis dans l'accueil
]
