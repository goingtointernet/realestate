# Generated by Django 4.0.4 on 2022-05-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_staticposts_page_name_alter_staticposts_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticposts',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='staticposts',
            name='page_name',
            field=models.CharField(default='Un-Named', max_length=70),
        ),
    ]
