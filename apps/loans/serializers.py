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
