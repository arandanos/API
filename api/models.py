from unittest.util import _MAX_LENGTH
from django.db import models

from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class AccesibleElement(models.Model):
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
    _name = models.ForeignKey("AccesibleElement", on_delete = models.CASCADE)
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
    _class_code = models.ForeignKey("AccesibleElement", on_delete = models.CASCADE)
    
    class Meta:
        _id = ['_id']
        _class_code = ['_class_code']
 
    def __str__(self):
        json_str = {
            "_id" : self._id,
            "_class_code" : self._class_code
        }
        return json_str

class Task(models.Model):
    _id = models.AutoField(primary_key = True)
    _name = models.ForeignKey("AccesibleElement", on_delete = models.CASCADE)
    _due_date = models.DateField()
    _feedback = models.TextField()
    
    class Meta:
        _id = ['_id']
        _name = ['_name']
        _due_date = ['_due_date']
        _feedback = ['_feedback']
 
    def __str__(self):
        json_str = {
            "_id" : self._id,
            "_name" : self._name,
            "_due_date" : self._due_date,
            "_feedback" : self._feedback
        }
        return json_str

class KitchenOrder(models.Model):
    _id = models.ForeignKey("Task", on_delete = models.CASCADE)
    
    class Meta:
        _id = ['_id']
 
    def __str__(self):
        json_str = {
            "_id" : self._id
        }
        return json_str

class KitchenOrderDetail(models.Model):
    _id = models.AutoField(primary_key = True)
    _class = models.ForeignKey("AccesibleElement", on_delete = models.CASCADE)
    _dish = models.ForeignKey("Dish", on_delete = models.CASCADE)
    _quantity = models.DateField()
    _kitchen_order = models.ForeignKey("KitchenOrder", on_delete = models.CASCADE)