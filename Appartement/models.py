from django.db import models

# Create your models here.


class Appartement(models.Model):

    adresse = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    surface = models.IntegerField(max_length=2, default=0)

    def __str__(self):
        return self.adresse
