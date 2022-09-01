# Generated by Django 4.0.4 on 2022-05-15 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=160)),
                ('b_content', models.TextField()),
                ('b_slug', models.CharField(max_length=70)),
                ('b_property_img1', models.ImageField(blank=True, null=True, upload_to='static/images/property')),
                ('b_property_img2', models.ImageField(blank=True, null=True, upload_to='static/images/property')),
                ('b_property_img3', models.ImageField(blank=True, null=True, upload_to='static/images/property')),
                ('b_thumbnail', models.ImageField(blank=True, null=True, upload_to='static/images/property')),
                ('b_property_price', models.FloatField(max_length=160)),
                ('b_room', models.FloatField(max_length=4)),
                ('b_bathroom', models.FloatField(max_length=4)),
                ('b_kitchen', models.FloatField(max_length=4)),
                ('b_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]