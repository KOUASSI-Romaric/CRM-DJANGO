import django_filters
from .models import Produit


class ProduitFiltre(django_filters.FilterSet):
    class Meta:
        model = Produit
        fields = '__all__'
        exclude = ['date_creation']
