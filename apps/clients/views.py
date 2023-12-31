from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.clients.filter import ClientFilter
from apps.clients.models import Client
from apps.clients.serializers import ClientSerializer
from config.permissions import OfficePermission


@extend_schema(tags=["client-api"])
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filterset_class = ClientFilter
    permission_classes = [IsAuthenticated, OfficePermission]
