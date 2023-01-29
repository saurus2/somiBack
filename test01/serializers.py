from rest_framework.serializers import ModelSerializer
from .models import Items

class TestDataSerializer(ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'