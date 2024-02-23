from django.db import models
from django.utils import timezone
from User.models import User

from Appartement.models import Appartement


class Visite(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    appartement = models.ForeignKey(Appartement, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    is_confirmed = models.BooleanField(default=True)

    def __str__(self):
        return f"Visit by {self.client} to {self.appartement} at {self.date}"
