# Generated by Django 3.1.2 on 2020-10-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0013_drug_minimum_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='ref_code',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
