# Generated by Django 4.0.4 on 2022-05-21 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0016_rename_monthly_instalment_buyproperty_lease_complete_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyproperty',
            old_name='lease_complete_price',
            new_name='instalment',
        ),
    ]
