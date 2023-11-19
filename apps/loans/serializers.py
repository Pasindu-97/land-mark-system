from rest_framework import serializers

from apps.clients.serializers import ClientSerializer
from apps.loans.models import (
    Investor,
    Loan,
    LoanFile,
    LoanGroup,
    LoanImage,
    Payment,
    ReleaseDate,
)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanGroup
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


class LoanSerializer(serializers.ModelSerializer):
    customer = ClientSerializer()
    guarantees = ClientSerializer(many=True)

    class Meta:
        model = Loan
        fields = (
            "id",
            "customer",
            "guarantees",
            "loan_group",
            "payment_start_date",
            "payment_period",
            "installment",
            "amount",
            "payable_amount",
            "interest_rate",
            "arrears",
            "status",
        )
        read_only_fields = ("id", "installment", "payable_amount", "arrears", "created", "modified", "created_by")


class LoanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = (
            "customer",
            "guarantees",
            "loan_group",
            "payment_start_date",
            "payment_period",
            "installment",
            "amount",
            "payable_amount",
            "interest_rate",
            "arrears",
            "status",
        )
        read_only_fields = ("id", "installment", "payable_amount", "arrears", "created", "modified", "created_by")


class LoanFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanFile
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


class LoanImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanImage
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


class BillSerializer(serializers.Serializer):
    customer = ClientSerializer()
    current_payment = serializers.DecimalField(max_digits=15, decimal_places=2)
    installment = serializers.DecimalField(max_digits=15, decimal_places=2)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    payable_amount = serializers.DecimalField(max_digits=15, decimal_places=2)
    arrears = serializers.DecimalField(max_digits=15, decimal_places=2)


class ReleaseDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseDate
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


class DashboardSerializer(serializers.Serializer):
    total_cash_out = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_cash_in = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_profit = serializers.DecimalField(max_digits=10, decimal_places=2)
