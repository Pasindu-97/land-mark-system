# Generated by Django 4.2.2 on 2023-10-09 16:27

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0010_remove_loangroup_investors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=127, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Investor',
                'verbose_name_plural': 'Investors',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='loangroup',
            name='investors',
            field=models.ManyToManyField(related_name='loan_groups', to='loans.investor', verbose_name='Investors'),
        ),
    ]
