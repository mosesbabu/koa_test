from rest_framework import serializers
from .models import Point

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('coordinates',)

    coordinates = serializers.ListField(child=serializers.CharField())

    def to_representation(self, instance):
        return instance

    def to_internal_value(self, data):
        return data