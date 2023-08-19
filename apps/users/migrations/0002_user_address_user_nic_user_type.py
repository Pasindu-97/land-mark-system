# Generated by Django 4.2.2 on 2023-08-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=1023, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='user',
            name='nic',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='NIC'),
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(blank=True, choices=[('ADMIN', 'Admin'), ('OFFICE_STAFF', 'Office Staff'), ('COLLECTOR', 'Collector'), ('INVESTOR', 'Investor')], default='OFFICE_STAFF', max_length=50, null=True, verbose_name='Type'),
        ),
    ]
