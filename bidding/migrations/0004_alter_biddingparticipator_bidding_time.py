# Generated by Django 4.0.4 on 2022-08-10 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0003_alter_biddingparticipator_bidding_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biddingparticipator',
            name='bidding_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 10, 9, 40, 35, 776699)),
        ),
    ]
