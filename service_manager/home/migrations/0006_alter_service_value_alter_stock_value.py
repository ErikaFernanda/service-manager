# Generated by Django 4.2.6 on 2023-11-19 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_service_value_stock_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stock',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]