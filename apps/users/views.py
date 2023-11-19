from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.serializers import UserCreateSerializer, UserViewSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return UserViewSerializer
        return UserCreateSerializer

    def perform_create(self, serializer):
        raw_password = self.request.data.get("password")
        hashed_password = make_password(raw_password)
        serializer.validated_data["password"] = hashed_password
        serializer.save()
