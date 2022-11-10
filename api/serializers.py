from dataclasses import fields
from rest_framework import serializers
from .models import AccessibleElement, DishType, Dish, Classroom, Feedback, Task, KitchenOrder, KitchenOrderDetail
 
class AccessibleElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessibleElement
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

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['_id', '_feedback']
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['_id', '_name', '_due_date', '_feedback']
        
class KitchenOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenOrder
        fields = ['_id', '_task']

class KitchenOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenOrderDetail
        fields = ['_id', '_classroom', '_dish', '_quantity', '_kitchen_order']