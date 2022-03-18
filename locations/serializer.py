from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ['id', 'visitor', 'place', 'description', 'created_at', 'updated_at', ]
    model = Location
