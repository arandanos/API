from rest_framework import serializers
from .models import AccesibleElement, DishType
 
class AccesibleElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccesibleElement
        fields = ['_id', '_text', '_pictogram']
        
class DishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishType
        fields = ['_id']