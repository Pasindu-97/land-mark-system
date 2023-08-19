from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Client(TimeStampedModel, models.Model):
    first_name = models.CharField(_("First Name"), max_length=127)
    last_name = models.CharField(_("Last Name"), max_length=127)
    nic = models.CharField(_("NIC"), max_length=15)
    address = models.CharField(_("Address"), max_length=1023)
    shop_name = models.CharField(_("Shop Name"), max_length=127)
    phone_number = models.CharField(_("Phone Number"), max_length=15)
    route = models.CharField(_("Route"), max_length=63, null=True, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return f"LM{self.id}"
