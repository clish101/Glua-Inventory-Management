from django.db import models


class Drug(models.Model):
    """Model definition for Drug."""
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Drug."""

        verbose_name = 'Drug'
        verbose_name_plural = 'Drugs'

    def __str__(self):
        """Unicode representation of Drug."""
        return self.name
