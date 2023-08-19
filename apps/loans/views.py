from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from apps.loans.models import Loan, LoanFile, LoanImage, Payment, ReleaseDate
from apps.loans.serializers import (
    LoanFileSerializer,
    LoanImageSerializer,
    LoanSerializer,
    PaymentSerializer,
    ReleaseDateSerializer,
)


@extend_schema(tags=["loan-api"])
class LoanViewSet(ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


@extend_schema(tags=["loan-file-api"])
class LoanFileViewSet(ModelViewSet):
    queryset = LoanFile.objects.all()
    serializer_class = LoanFileSerializer


@extend_schema(tags=["loan-image-api"])
class LoanImageViewSet(ModelViewSet):
    queryset = LoanImage.objects.all()
    serializer_class = LoanImageSerializer


@extend_schema(tags=["payment-api"])
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


@extend_schema(tags=["Release-date-api"])
class ReleaseDateViewSet(ModelViewSet):
    queryset = ReleaseDate.objects.all()
    serializer_class = ReleaseDateSerializer
