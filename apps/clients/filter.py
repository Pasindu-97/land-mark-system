import django_filters

from apps.clients.models import Client


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ["nic"]
