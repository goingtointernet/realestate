# Generated by Django 4.0.4 on 2022-05-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_rename_b_author_buyproperty_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyproperty',
            name='floor',
            field=models.FloatField(default=0.0, max_length=4),
        ),
        migrations.AddField(
            model_name='buyproperty',
            name='marla',
            field=models.FloatField(default=0.0, max_length=4),
        ),
    ]