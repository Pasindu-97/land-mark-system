# Generated by Django 4.2.2 on 2023-08-23 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0007_auto_20230823_1607'),
    ]

    operations = [
        migrations.RenameField('Loan', 'group', 'loan_group')
    ]