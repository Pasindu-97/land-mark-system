# Generated by Django 4.2.2 on 2023-08-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0004_alter_loan_arrears'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='payed_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Amount'),
        ),
    ]
