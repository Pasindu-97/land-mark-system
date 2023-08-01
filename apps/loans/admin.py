from django.contrib import admin

from apps.loans.models import Loan, LoanFile, LoanImage, Payment, ReleaseDate
from config.admin import custom_admin_site


@admin.register(Loan, site=custom_admin_site)
class LoanAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment, site=custom_admin_site)
class PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(LoanFile, site=custom_admin_site)
class LoanFileAdmin(admin.ModelAdmin):
    pass


@admin.register(LoanImage, site=custom_admin_site)
class LoanImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ReleaseDate, site=custom_admin_site)
class ReleaseDateAdmin(admin.ModelAdmin):
    pass
