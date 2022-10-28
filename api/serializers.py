from rest_framework import serializers
from .models import AccesibleElement, DishType, Dish, Classroom
 
class AccesibleElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccesibleElement
        fields = ['_id', '_text', '_pictogram']
        
class DishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishType
        fields = ['_id']
        
class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['_id', '_name', '_type']
        
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['_id', '_class_code']