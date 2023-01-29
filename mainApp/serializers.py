from rest_framework import serializers
from .models import Review

# DRF: Django REST Framework for connection Django and React
# Serializer is class of DRF, DB instance will be by JSON
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'updated_at')
