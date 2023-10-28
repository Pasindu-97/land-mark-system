import django_filters

from apps.clients.models import Client


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ["nic", "first_name", "last_name", "phone_number"]
