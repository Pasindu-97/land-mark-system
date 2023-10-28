import decimal
from datetime import date

from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.loans.filter import LoanFilter
from apps.loans.models import (
    Investor,
    Loan,
    LoanFile,
    LoanGroup,
    LoanImage,
    Payment,
    ReleaseDate,
)
from apps.loans.serializers import (
    GroupSerializer,
    InvestorSerializer,
    LoanCreateSerializer,
    LoanFileSerializer,
    LoanImageSerializer,
    LoanSerializer,
    PaymentSerializer,
    ReleaseDateSerializer,
)


@extend_schema(tags=["loan-api"])
class LoanViewSet(ModelViewSet):
    queryset = Loan.objects.all()
    filterset_class = LoanFilter

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return LoanSerializer
        return LoanCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        loan_amount = decimal.Decimal(serializer.validated_data["amount"])
        loan_interest_rate = decimal.Decimal(serializer.validated_data["interest_rate"])
        loan_period = int(serializer.validated_data["payment_period"])

        monthly_installment = (loan_amount / loan_period * 30) + (loan_amount * loan_interest_rate / 100)
        daily_installment = monthly_installment / 30
        serializer.validated_data["installment"] = decimal.Decimal(daily_installment)
        serializer.validated_data["payable_amount"] = loan_amount
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @extend_schema(
        # extra parameters added to the schema
        parameters=[
            OpenApiParameter(name="start_date", required=False, type=date),
            OpenApiParameter(name="end_date", required=False, type=date),
        ]
    )
    def list(self, request, *args, **kwargs):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")
        print(start_date, end_date)

        if start_date is not None and end_date is not None:
            queryset = self.queryset.filter(created__range=(start_date, end_date))
        else:
            queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@extend_schema(tags=["loan-file-api"])
class LoanFileViewSet(ModelViewSet):
    queryset = LoanFile.objects.all()
    serializer_class = LoanFileSerializer(many=True)


@extend_schema(tags=["loan-image-api"])
class LoanImageViewSet(ModelViewSet):
    queryset = LoanImage.objects.all()
    serializer_class = LoanImageSerializer(many=True)
    parser_classes = (MultiPartParser,)


@extend_schema(tags=["payment-api"])
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        loan = serializer.validated_data["loan"]
        payment_amount = decimal.Decimal(serializer.validated_data["amount"])

        loan.arrears += loan.installment - payment_amount
        loan.payable_amount -= payment_amount
        if loan.payable_amount <= 0:
            loan.status = Loan.Statuses.COMPLETED
        loan.save()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@extend_schema(tags=["release-date-api"])
class ReleaseDateViewSet(ModelViewSet):
    queryset = ReleaseDate.objects.all()
    serializer_class = ReleaseDateSerializer


@extend_schema(tags=["loan-group-api"])
class LoanGroupViewSet(ModelViewSet):
    queryset = LoanGroup.objects.all()
    serializer_class = GroupSerializer


@extend_schema(tags=["investor-api"])
class InvestorViewSet(ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
