from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class AccessibleElement(models.Model):
    _id = models.AutoField(primary_key = True)
    _text = models.TextField()
    _pictogram = models.TextField()
    
    class Meta:
        _id = ['_id']
        _text = ['_text']
        _pictogram = ['_pictogram']
 
    def __str__(self):
        json_str = {
            "_id" : self._id,
            "_text" : self._text,
            "_pictogram" : self._pictogram
        }
        return json_str

class DishType(models.Model):
    _id = models.CharField(primary_key = True, max_length = 20)
    
    class Meta:
        _id = ['_id']
 
    def __str__(self):
        json_str = {
            "_id" : self._id
        }
        return json_str

class Dish(models.Model):
    _id = models.AutoField(primary_key = True)
    _name = models.ForeignKey("AccessibleElement", on_delete = models.CASCADE)
    _type = models.ForeignKey("DishType", on_delete = models.CASCADE)
    
    class Meta:
        _id = ['_id']
        _name = ['_name']
        _type = ['_type']
 
    def __str__(self):
        json_str = {
            "_id" : self._id,
            "_name" : self._name,
            "_type" : self._type
        }
        return json_str

class Classroom(models.Model):
    _id = models.AutoField(primary_key = True)
    _class_code = models.ForeignKey("AccessibleElement", on_delete = models.CASCADE)
    
    class Meta:
        _id = ['_id']
        _class_code = ['_class_code']
 
    def __str__(self):
        json_str = {
            "_id" : self._id,
            "_class_code" : self._class_code
        }
        return json_str

class Feedback(models.Model):
    _id = models.AutoField(primary_key = True)
    _feedback = models.ForeignKey("AccessibleElement", on_delete = models.CASCADE)

    class Meta:
        _id = ['_id']
        _feedback = ['_feedback']
 
    def __str__(self):
        json_str = {
            "_id" : self._id,
            "_feedback" : self._feedback
        }
        return json_str

class Task(models.Model):
    _id = models.AutoField(primary_key = True)
    _name = models.ForeignKey("AccessibleElement", on_delete = models.CASCADE)
    _due_date = models.DateField()
    _feedback = models.ForeignKey("Feedback", on_delete = models.CASCADE, null=True, blank=True)
    _type = models.TextField()
    _status = models.BooleanField(default=False)
    
    class Meta:
        _id = ['_id']
        _name = ['_name']
        _due_date = ['_due_date']
        _feedback = ['_feedback']
        _type = ['_type']
        _status = ['_status']
 
    def __str__(self):
        json_str = {
            "_id" : self._id,
            "_name" : self._name,
            "_due_date" : self._due_date,
            "_feedback" : self._feedback,
            "_type" : self._type,
            "_status" : self._status
        }
        return json_str

class KitchenOrder(models.Model):
    _id = models.AutoField(primary_key = True)
    _task = models.ForeignKey("Task", on_delete = models.CASCADE)
    
    class Meta:
        _id = ['_id']
        _taks = ['_task']
 
    def __str__(self):
        json_str = {
            "_id" : self._id,
            "_task" : self._task
        }
        return json_str

class KitchenOrderDetail(models.Model):
    _id = models.AutoField(primary_key = True)
    _classroom = models.ForeignKey("Classroom", on_delete = models.CASCADE)
    _dish = models.ForeignKey("Dish", on_delete = models.CASCADE)
    _quantity = models.IntegerField()
    _kitchen_order = models.ForeignKey("KitchenOrder", on_delete = models.CASCADE)
    
    class Meta:
        _id = ['_id']
        _classroom = ['_classroom']
        _dish = ['_dish']
        _quantity = ['_quantity']
        _kitchen_order = ['_kitchen_order']
 
    def __str__(self):
        json_str = {
            "_id" : self._id,
            "_classroom" : self._classroom,
            "_dish" : self._dish,
            "_quantity" : self._quantity,
            "_kitchen_order" : self._kitchen_order
        }
        return json_str