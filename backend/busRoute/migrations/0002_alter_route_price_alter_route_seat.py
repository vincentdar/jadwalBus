# Generated by Django 4.2.5 on 2023-09-19 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busRoute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='route',
            name='seat',
            field=models.BigIntegerField(blank=True, default=20),
        ),
    ]
