from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Drug(models.Model):
    """Model definition for Drug."""
    name = models.CharField(unique=True, max_length=200)
    buying_price = models.FloatField()
    selling_price= models.FloatField(null=True)
    maximum_price = models.FloatField()
    stock = models.IntegerField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Drug."""

        verbose_name = 'Drug'
        verbose_name_plural = 'Drugs'

    def __str__(self):
        """Unicode representation of Drug."""
        return self.name

    def save(self, *args, **kwargs):
            for field_name in ['name']:
                val = getattr(self, field_name, False)
                if val:
                    setattr(self, field_name, val.capitalize())
            super(Drug, self).save(*args, **kwargs)

class Sale(models.Model):
    seller = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    drug_sold = models.ForeignKey(Drug, on_delete=models.PROTECT)
    date_sold = models.DateField(default=timezone.now)
    # date_sold = models.DateField(auto_now_add=True, blank=True, null=True)
    sale_price = models.FloatField(null=True, blank=True)
    buying_price = models.FloatField(null=True, blank=True)
    """Model definition for Sale."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Sale."""

        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return f'{self.drug_sold} sold on {self.date_sold}'
