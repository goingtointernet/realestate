# Generated by Django 4.0.4 on 2022-05-24 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=70, unique=True)),
            ],
        ),
    ]
