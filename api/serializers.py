from dataclasses import fields
from rest_framework import serializers
from .models import *
 
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
        fields = ['_id', '_name']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['_id', '_feedback']
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['_id', '_name', '_due_date', '_feedback', '_type', '_status', '_auto_feedback']
        
class KitchenOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenOrder
        fields = ['_id', '_task', '_auto_calc']

class KitchenOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenOrderDetail
        fields = ['_id', '_classroom', '_dish', '_quantity', '_kitchen_order']

class MaterialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialType
        fields = ['_id', '_item']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['_id', '_type', '_color', '_quantity']

class MaterialTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialTask
        fields = ['_id', '_task', '_classroom']

class MaterialTaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialTaskDetail
        fields = ['_id', '_material_task', '_material', '_task_quantity']