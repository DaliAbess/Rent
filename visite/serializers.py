from rest_framework import serializers
from .models import Visite


class VisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visite
        fields = ['id', 'client', 'appartement', 'date', 'is_confirmed']
