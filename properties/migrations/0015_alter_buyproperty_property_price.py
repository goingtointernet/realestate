# Generated by Django 4.0.4 on 2022-05-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0014_remove_buyproperty_lease_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyproperty',
            name='property_price',
            field=models.IntegerField(default=0),
        ),
    ]
