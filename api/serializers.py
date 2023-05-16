from rest_framework import serializers
from .models import Points

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ('points',)
