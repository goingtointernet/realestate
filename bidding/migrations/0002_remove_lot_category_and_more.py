# Generated by Django 4.0.4 on 2022-06-01 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='category',
        ),
        migrations.AlterField(
            model_name='biddingparticipator',
            name='bidding_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 3, 52, 2, 756364)),
        ),
    ]
