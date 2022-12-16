from dataclasses import fields
from rest_framework import serializers
from .models import *
 
class AccessibleElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessibleElement
        fields = ['_id', '_text', '_pictogram', '_alt']
        
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
        fields = ['_id', '_name']
        
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
        fields = ['_id', '_name']

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
        fields = ['_id', '_material_task', '_material', '_quantity']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['_id', '_name']


class PrinterLaminatorTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterLaminatorTask
        fields = ['_id', '_task', '_classroom', '_color', '_quantity']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['_id', '_username', '_name', '_password', '_is_admin']

class TeachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teach
        fields = ['_id', '_teacher', '_classroom']

class AccessibleModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessibleMode
        fields = ['_id']

class TextSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextSize
        fields = ['_id']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['_id', '_name', '_accessible_mode', '_text_size', '_password', '_caps', '_is_pass_pictogram', '_pass_in_order']

class PasswordPictogramSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordPictogram
        fields = ['_id', '_student', '_digit']