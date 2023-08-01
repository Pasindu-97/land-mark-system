from django.contrib import admin

from apps.clients.models import Client
from config.admin import custom_admin_site


@admin.register(Client, site=custom_admin_site)
class ClientAdmin(admin.ModelAdmin):
    pass
