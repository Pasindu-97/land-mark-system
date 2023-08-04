from rest_framework import serializers

from apps.loans.models import Group, Loan, LoanFile, LoanImage, Payment, ReleaseDate


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


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
