# Generated by Django 4.0.4 on 2022-05-14 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_bio_user_profile_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
