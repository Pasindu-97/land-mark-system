import django_filters

from apps.loans.models import Loan


class LoanFilter(django_filters.FilterSet):
    class Meta:
        model = Loan
        fields = ["customer", "loan_group", "status", "payment_period"]
