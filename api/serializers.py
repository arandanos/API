from rest_framework import serializers
from .models import AccesibleElement
 
class AccesibleElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccesibleElement
        fields = ['_id', '_text', '_pictogram']