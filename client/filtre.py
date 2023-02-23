import django_filters
from .models import Client


class ClientFiltre(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['date_creation']
