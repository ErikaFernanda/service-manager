# Generated by Django 4.2.6 on 2023-12-10 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_customer_service_note_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='cnpj',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
