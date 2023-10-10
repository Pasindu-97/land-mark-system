from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.serializers import UserCreateSerializer, UserViewSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return UserViewSerializer
        return UserCreateSerializer
