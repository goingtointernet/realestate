# Generated by Django 4.0.4 on 2022-05-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='static/images/default_profile.png', null=True, upload_to='static/images'),
        ),
    ]
