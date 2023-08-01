from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import UUIDModel


class User(UUIDModel, models.Model, AbstractUser):
    class Types(models.TextChoices):
        ADMIN = "ADMIN", _("Admin")
        OFFICE_STAFF = "OFFICE_STAFF", _("Office Staff")
        COLLECTOR = "COLLECTOR", _("Collector")
        INVESTOR = "INVESTOR", _("Investor")

    nic = models.CharField(_("NIC"), max_length=15)
    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=Types.OFFICE_STAFF)
    address = models.CharField(_("Address"), max_length=1023, null=True, blank=True)

    class Meta:
        ordering = ["-date_joined"]
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return str(self.get_full_name())
