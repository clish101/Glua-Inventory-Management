# Generated by Django 3.1.2 on 2020-10-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_auto_20201011_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]