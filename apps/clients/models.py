from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel, UUIDModel


class Client(UUIDModel, TimeStampedModel, models.Model):
    id = models.CharField(_("Id"), max_length=10, unique=True, primary_key=True)
    first_name = models.CharField(_("First Name"), max_length=127)
    last_name = models.CharField(_("Last Name"), max_length=127)
    nic = models.CharField(_("NIC"), max_length=15)
    address = models.CharField(_("Address"), max_length=1023)
    shop_name = models.CharField(_("Shop Name"), max_length=127)
    phone_number = models.CharField(_("Phone Number"), max_length=15)
    route = models.CharField(_("Route"), max_length=63, null=True, blank=True)

    def generate_id(self):
        latest_client = Client.objects.order_by("-id").first()
        if latest_client:
            latest_id_num = int(latest_client.id[2:])
            new_id_num = latest_id_num + 1
        else:
            new_id_num = 1
        return f"LM{new_id_num}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_id()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return str(self.id)
