# Generated by Django 4.0.4 on 2022-05-24 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_footerdata_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerdata',
            name='address',
            field=models.CharField(max_length=260, null=True),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='copyright',
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='facebook',
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='instagram',
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='made_by',
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='twitter',
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='footerdata',
            name='youtube',
            field=models.CharField(max_length=160, null=True),
        ),
    ]
