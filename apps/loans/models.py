from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from apps.clients.models import Client


class LoanGroup(TimeStampedModel, models.Model):
    investors = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="investor_groups", verbose_name=_("Investors")
    )
    name = models.CharField(_("Name"), max_length=127)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Loan Group")
        verbose_name_plural = _("Loan Groups")

    def __str__(self):
        return f"LM_GROUP{self.id}"


class Loan(TimeStampedModel, models.Model):
    class Statuses(models.TextChoices):
        PENDING = "PENDING", _("Pending")
        APPROVED = "APPROVED", _("Approved")
        ARREARS = "ARREARS", _("Arrears")
        CLOSED = "CLOSED", _("Closed")
        COMPLETED = "COMPLETED", _("Completed")

    customer = models.ForeignKey(Client, models.CASCADE, related_name="loans", verbose_name=_("Customer"))
    guarantees = models.ManyToManyField(Client, verbose_name=_("Guarantees"))
    loan_group = models.ForeignKey(
        LoanGroup, models.CASCADE, related_name="loans", verbose_name=_("Group"), null=True, blank=True
    )

    payment_start_date = models.DateTimeField(_("Payment Start Date"))
    payment_period = models.IntegerField(_("Payment Period"))
    installment = models.DecimalField(_("Installment"), max_digits=15, decimal_places=2)

    amount = models.DecimalField(_("Amount"), max_digits=15, decimal_places=2)
    payable_amount = models.DecimalField(_("Amount"), max_digits=15, decimal_places=2, default=0)
    interest_rate = models.DecimalField(_("Interest Rate"), max_digits=4, decimal_places=2)
    arrears = models.DecimalField(_("Arrears"), max_digits=15, decimal_places=2, default=0)
    status = models.CharField(_("Status"), max_length=50, choices=Statuses.choices, default=Statuses.PENDING)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Loan")
        verbose_name_plural = _("Loans")

    def __str__(self):
        return f"LM_LOAN{self.id}"


class LoanFile(TimeStampedModel, models.Model):
    file = models.FileField(_("File"))
    loan = models.ForeignKey(Loan, models.CASCADE, related_name="loan_files", verbose_name=_("Loan"))

    class Meta:
        ordering = ["id"]
        verbose_name = _("Loan File")
        verbose_name_plural = _("Loan Files")

    def __str__(self):
        return f"LM_FILE{self.id}"


class LoanImage(TimeStampedModel, models.Model):
    image = models.ImageField(_("image"))
    loan = models.ForeignKey(Loan, models.CASCADE, related_name="loan_images", verbose_name=_("Loan"))

    class Meta:
        ordering = ["id"]
        verbose_name = _("Loan Image")
        verbose_name_plural = _("Loan Images")

    def __str__(self):
        return f"LM_IMAGE{self.id}"


class Payment(TimeStampedModel, models.Model):
    class PaymentModes(models.TextChoices):
        CASH = "CASH", _("Cash")
        BANK_TRANSFER = "BANK_TRANSFER", _("Bank Transfer")
        CHEQUE = "CHEQUE", _("Cheque")

    loan = models.ForeignKey(Loan, models.CASCADE, related_name="payments", verbose_name=_("Loan"))
    collector = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.CASCADE, related_name="payments", verbose_name=_("Collector")
    )

    amount = models.DecimalField(_("Amount"), max_digits=15, decimal_places=2)
    payment_mode = models.CharField(
        _("Payment Mode"), max_length=50, choices=PaymentModes.choices, default=PaymentModes.CASH
    )

    class Meta:
        ordering = ["id"]
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return f"LM_PAYMENT{self.id}"


class ReleaseDate(TimeStampedModel, models.Model):
    class DateTypes(models.TextChoices):
        POYA = "POYA", _("Poya")
        OTHER = "OTHER", _("Other")

    type = models.CharField(_("Date Type"), max_length=50, choices=DateTypes.choices, default=DateTypes.POYA)
    date = models.DateField(_("Date"))
    note = models.CharField(_("Note"), max_length=127, null=True, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Release Date")
        verbose_name_plural = _("Release Dates")

    def __str__(self):
        return f"LM_RDATE{self.id}"
