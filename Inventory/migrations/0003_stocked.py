# Generated by Django 3.1.2 on 2020-10-11 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inventory', '0002_sale_buying_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('number_added', models.IntegerField()),
                ('Drug_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Inventory.drug')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
    ]
