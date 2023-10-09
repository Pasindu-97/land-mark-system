from drf_spectacular.utils import extend_schema
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from apps.clients.models import Client
from apps.clients.serializers import ClientSerializer


@extend_schema(tags=["client-api"])
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filter_backends = (SearchFilter,)
    search_fields = ("first_name",)
