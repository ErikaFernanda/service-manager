# Generated by Django 4.2.6 on 2023-12-06 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_companyuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Service_Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.BinaryField()),
            ],
        ),
    ]
