import json
from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import  *

# ******************************
# *     ACCESSIBLE ELEMENT     *
# ******************************

#· MÉTODOS AUXILIARES
# Devuelve el elemente de la base de datos que corresponda con el id
def getAccessibleElementByID(_id):
    item = AccessibleElement.objects.get(_id = _id)
    item_serializer = AccessibleElementSerializer(item)
    return item_serializer.data
    

# Peticiones GET y POST simples
@csrf_exempt
def AccessibleElementView(request):
    # Devuelve todos los elementos de la tabla Accessible_Element
    if request.method == 'GET':
        accessible_elements = AccessibleElement.objects.all().order_by('_id')
        serializer = AccessibleElementSerializer(accessible_elements, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    # Crea una nueva entrada en la tabla Accesible_Element si no hay ninguno con la misma información
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccessibleElementSerializer(data = data)
        
        already_in_db = AccessibleElement.objects.filter(_text = data['_text'], _pictogram = data['_pictogram'])
                
        if already_in_db:
            serializer = AccessibleElementSerializer(already_in_db[0])
            return JsonResponse(serializer.data, status = 201)
        elif serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)
    
# Peticiones GET y POST pasando una ID como argumento
@csrf_exempt
def AccessibleElementViewID(request, _id):
    # Comprobación de que existe un elemento en la tabla con la ID
    try: 
        item =  AccessibleElement.objects.get(_id = _id)
    # Si no existe se lanza un error 404
    except AccessibleElement.DoesNotExist:
        raise Http404('Not found')
    
    # Se devuelve la entrada de la tabla con igual ID
    if request.method == 'GET':
        serializer = AccessibleElementSerializer(item)
        return JsonResponse(serializer.data, safe = False)
    
    # Se modifica la entrada de la tabla con igual ID si no existe otro elemento que tenga la misma informacón tras modificar la entrada
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = AccessibleElementSerializer(item)
        
        if not('_text' in data):
            data['_text'] = item_serializer.data['_text']
            
        if not('_pictogram' in data):
            data['_pictogram'] = item_serializer.data['_pictogram']
        
        # Devuelve un array con todos los objetos cuyos valores sean los mismos que los argumentos
        already_in_db = AccessibleElement.objects.filter(_text = data['_text'], _pictogram = data['_pictogram'])
 
        if already_in_db:
            serializer = AccessibleElementSerializer(already_in_db[0])
            return JsonResponse(serializer.data, safe = False)
        else:
            serializer = AccessibleElementSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        
        return HttpResponse(status = 400)

    # Se elimina la entrada de la tabla con igual ID
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)
    
# *****************************
# *         DISH TYPE         *
# *****************************

@csrf_exempt
def DishTypeView(request):
    
    if request.method == 'GET':
        dish_types = DishType.objects.all().order_by('_id')
        serializer = DishTypeSerializer(dish_types, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['_id'] = str.upper(data['_id'])
        serializer = DishTypeSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)
        

@csrf_exempt
def DishTypeViewID(request, _id):
    # Comprobación de que existe un elemento en la tabla con la ID
    try: 
        item = DishType.objects.get(_id = str.upper(_id))
    # Si no existe se lanza un error 404
    except DishType.DoesNotExist:
        raise Http404('Not found')
    
    # Se devuelve la entrada de la tabla con igual ID
    if request.method == 'GET':
        serializer = DishTypeSerializer(item)
        return JsonResponse(serializer.data, safe = False)

    # Se modifica la entrada de la tabla con igual ID si no existe otro elemento que tenga la misma informacón tras modificar la entrada
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = DishTypeSerializer(item)
        
        # Devuelve un array con todos los objetos cuyos valores sean los mismos que los argumentos
        already_in_db = DishType.objects.filter(_id = item_serializer.data['_id'])
 
        if already_in_db:
            return JsonResponse(already_in_db, safe = False)
        else:
            serializer = DishTypeSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        
        return HttpResponse(status = 400)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)
        
    
    return HttpResponse(status = 400)

# ******************************
# *            DISH            *
# ******************************

@csrf_exempt
def DishView(request):
    if request.method == 'GET':
        dishes = Dish.objects.all().order_by('_id')
        serializer = DishSerializer(dishes, many = True)

        for dish in serializer.data:
            dish['_name'] = getAccessibleElementByID(dish['_name'])

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DishSerializer(data = data)
        
        already_in_db = Dish.objects.filter(_name = data['_name'], _type = data['_type'])
                
        if already_in_db:
            serializer = DishSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)
        
        data = serializer.data
        data['_name'] = getAccessibleElementByID(serializer.data['_name'])
        return JsonResponse(data, status = 201)
    
@csrf_exempt
def DishViewID(request, _id):

    try: 
        item = Dish.objects.get(_id = _id)

    except Dish.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = DishSerializer(item)
        serializer.data['_name'] = getAccessibleElementByID(serializer.data['_name'])
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = DishSerializer(item)
        
        if not('_name' in data):
            data['_name'] = item_serializer.data['_name']
            
        if not('_type' in data):
            data['_type'] = item_serializer.data['_type']
        
        already_in_db = Dish.objects.filter(_name = data['_name'], _type = data['_type'])
 
        if already_in_db:
            serializer = DishSerializer(already_in_db[0])
            return JsonResponse(serializer.data, safe = False)
        else:
            serializer = DishSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        
        return HttpResponse(status = 400)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)
    
# *****************************
# *         CLASSROOM         *
# *****************************

@csrf_exempt
def ClassroomView(request):
    if request.method == 'GET':
        classrooms = Classroom.objects.all().order_by('_id')
        serializer = ClassroomSerializer(classrooms, many = True)

        for classroom in serializer.data:
            classroom['_class_code'] = getAccessibleElementByID(classroom['_class_code'])

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClassroomSerializer(data = data)
        
        already_in_db = Classroom.objects.filter(_class_code = data['_class_code'])
                
        if already_in_db:
            serializer = ClassroomSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = serializer.data
        data['_class_code'] = getAccessibleElementByID(serializer.data['_class_code'])
        return JsonResponse(data, status = 201)

@csrf_exempt
def ClassroomViewID(request, _id):

    try: 
        item = Classroom.objects.get(_id = _id)

    except Classroom.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = ClassroomSerializer(item)
        data = serializer.data
        data['_class_code'] = getAccessibleElementByID(serializer.data['_class_code'])
        return JsonResponse(data, safe = False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = ClassroomSerializer(item)
        
        if not('_class_code' in data):
            data['_class_code'] = item_serializer.data['_class_code']
        
        already_in_db = Classroom.objects.filter(_class_code = data['_class_code'])
 
        if already_in_db:
            serializer = ClassroomSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer = ClassroomSerializer(item, data = data)
            serializer.save()
        else: 
            return HttpResponse(status = 400)
        
        data = serializer.data
        data['_class_code'] = getAccessibleElementByID(serializer.data['_class_code'])
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

# ****************************
# *         FEEDBACK         *
# ****************************

#· MÉTODOS AUXILIARES
def getFeedbackByID(_id):
    item = Feedback.objects.get(_id = _id)
    serializer = FeedbackSerializer(item)
    data = serializer.data
    data['_feedback'] = getAccessibleElementByID(serializer.data['_feedback'])
    return data

@csrf_exempt
def FeedbackView(request):
    if request.method == 'GET':
        feedbacks = Feedback.objects.all().order_by('_id')
        serializer = FeedbackSerializer(feedbacks, many = True)

        for feedback in serializer.data:
            feedback['_feedback'] = getAccessibleElementByID(feedback['_feedback'])

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedbackSerializer(data = data)
        
        already_in_db = Feedback.objects.filter(_feedback = data['_feedback'])
                
        if already_in_db:
            serializer = FeedbackSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = getFeedbackByID(serializer.data['_feedback'])
        return JsonResponse(data, status = 201)
    
# ****************************
# *           TASK           *
# ****************************

@csrf_exempt
def TaskView(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('_id')
        serializer = TaskSerializer(tasks, many = True)

        for task in serializer.data:
            task['_name'] = getAccessibleElementByID(task['_name'])
            task['_feedback'] = getFeedbackByID(task['_feedback'])

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data = data)

        already_in_db = Task.objects.filter(_name = data['_name'], _due_date = data['_due_date'])
                
        if '_feedback' in data:
            already_in_db = Task.objects.filter(_name = data['_name'], _due_date = data['_due_date'], _feedback = data['_feedback'])

        if already_in_db:
            serializer = TaskSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = serializer.data
        data['_name'] = getAccessibleElementByID(serializer.data['_name'])

        if '_feedback' in data:
            data['_feedback'] = getFeedbackByID(serializer.data['_feedback'])

        return JsonResponse(data, status = 201)
    
@csrf_exempt
def TaskViewID(request, _id):

    try: 
        item = Task.objects.get(_id = _id)

    except Task.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = TaskSerializer(item)
        
        data = serializer.data
        data['_name'] = getAccessibleElementByID(serializer.data['_name'])
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = TaskSerializer(item)
        
        if not('_name' in data):
            data['_name'] = item_serializer.data['_name']
            
        if not('_feedback' in data):
            data['_feedback'] = item_serializer.data['_feedback']
        
        if not('_type' in data):
            data['_type'] = item_serializer.data['_type']

        if not('_due_date' in data):
            data['_due_date'] = item_serializer.data['_due_date']
        
        if not('_status' in data):
            data['_status'] = item_serializer.data['_status']
            
        if not('_auto_feedback' in data):
            data['_auto_feedback'] = item_serializer.data['_auto_feedback']
        
        already_in_db = Task.objects.filter(_name = data['_name'], _feedback = data['_feedback'], _type = data['_type'], _due_date = data['_due_date'], _status = data['_status'], _auto_feedback = data['_auto_feedback'])
 
        if already_in_db:
            serializer = TaskSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer = TaskSerializer(item, data = data)
            serializer.save()
        else:
            return HttpResponse(status = 400)

        data = serializer.data
        data['_name'] = getAccessibleElementByID(serializer.data['_name'])

        if 'feedback' in data:
            data['_feedback'] = getFeedbackByID(serializer.data['_feedback'])

        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)
    
# ***************************
# *      KITCHEN ORDER      *
# ***************************

@csrf_exempt
def KitchenOrderView(request):
    
    if request.method == 'GET':
        kitchen_orders = KitchenOrder.objects.all().order_by('_id')
        serializer = KitchenOrderSerializer(kitchen_orders, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = KitchenOrderSerializer(data = data)
        
        already_in_db = KitchenOrder.objects.filter(_task = data['_task'], _auto_calc = data['_auto_calc'])
                
        if already_in_db:
            serializer = KitchenOrderSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)
        
        return JsonResponse(serializer.data, status = 201)
    
@csrf_exempt
def KitchenOrderViewID(request, _id):

    try: 
        item = KitchenOrder.objects.get(_id = _id)
    except AccessibleElement.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = KitchenOrderSerializer(item)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

# ********************************
# *     KITCHEN ORDER DETAIL     *
# ********************************

@csrf_exempt
def KitchenOrderDetailView(request):
    
    if request.method == 'GET':
        kitchen_orders_deatils = KitchenOrderDetail.objects.all().order_by('_id')
        serializer = KitchenOrderDetailSerializer(kitchen_orders_deatils, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = KitchenOrderDetailSerializer(data = data)
        
        already_in_db = KitchenOrderDetail.objects.filter(_classroom = data['_classroom'], _dish = data['_dish'], _quantity = data['_quantity'], _kitchen_order = data['_kitchen_order'])
                
        if already_in_db:
            serializer = KitchenOrderDetailSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)
        
        return JsonResponse(serializer.data, status = 201)

@csrf_exempt
def KitchenOrderDetailViewID(request, _id):

    try: 
        item = KitchenOrderDetail.objects.get(_id = _id)

    except KitchenOrderDetail.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = KitchenOrderDetailSerializer(item)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = KitchenOrderDetailSerializer(item)
        
        if not('_classroom' in data):
            data['_classroom'] = item_serializer.data['_classroom']
            
        if not('_dish' in data):
            data['_dish'] = item_serializer.data['_dish']
            
        if not('_quantity' in data):
            data['_quantity'] = item_serializer.data['_quantity']
        
        if not('_kitchen_order' in data):
            data['_kitchen_order'] = item_serializer.data['_kitchen_order']
        
        already_in_db = KitchenOrderDetail.objects.filter(_classroom = data['_classroom'], _dish = data['_dish'], _quantity = data['_quantity'], _kitchen_order = data['_kitchen_order'])
 
        if already_in_db:
            serializer = KitchenOrderDetailSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer = KitchenOrderDetailSerializer(item, data = data)
            serializer.save()
        else: 
            return HttpResponse(status = 400)
        
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)


# *****************************
# *       MATERIAL TYPE       *
# *****************************

@csrf_exempt
def MaterialTypeView(request):
    if request.method == 'GET':
        material_types = MaterialType.objects.all().order_by('_id')
        serializer = MaterialTypeSerializer(material_types, many = True)

        for material_type in serializer.data:
            material_type['_item'] = getAccessibleElementByID(material_type['_item'])

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MaterialTypeSerializer(data = data)
        
        already_in_db = MaterialType.objects.filter(_item = data['_item'])
                
        if already_in_db:
            serializer = MaterialTypeSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)
        
        return JsonResponse(serializer.data, status = 201)

# **************************
# *        MATERIAL        *
# **************************

@csrf_exempt
def MaterialView(request):
    
    if request.method == 'GET':
        materials = Material.objects.all().order_by('_id')
        serializer = MaterialSerializer(materials, many = True)

        for material in serializer.data:
            material['_color'] = getAccessibleElementByID(material['_color'])

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MaterialSerializer(data = data)
        
        already_in_db = Material.objects.filter(_item = data['_item'], _color = data['_color'])
                
        if already_in_db:
            serializer = KitchenOrderSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)
        
        data = serializer.data
        data['_color'] = getAccessibleElementByID(serializer.data['_color'])
        return JsonResponse(serializer.data, status = 201)
    
@csrf_exempt
def MaterialViewID(request, _id):

    try: 
        item = Material.objects.get(_id = _id)
    except Material.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = MaterialSerializer(item)
        data = serializer.data
        data['_color'] = getAccessibleElementByID(serializer.data['_color'])
        return JsonResponse(data, safe = False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = MaterialSerializer(item)
        
        if not('_item' in data):
            data['_item'] = item_serializer.data['_item']

        if not('_color' in data):
            data['_color'] = item_serializer.data['_color']

        if not('_quantity' in data):
            data['_quantity'] = item_serializer.data['_quantity']
        
        already_in_db = Material.objects.filter(_item = data['_item'], _color = data['_color'], _quantity = data['_quantity'])
 
        if already_in_db:
            serializer = MaterialSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer = MaterialSerializer(item, data = data)
            serializer.save()
        else: 
            return HttpResponse(status = 400)
        
        data = serializer.data
        data['_color'] = getAccessibleElementByID(serializer.data['_color'])
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

# ***************************
# *      MATERIAL TASK      *
# ***************************

@csrf_exempt
def MaterialTaskView(request):
    
    if request.method == 'GET':
        materials = MaterialTask.objects.all().order_by('_id')
        serializer = MaterialTaskSerializer(materials, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MaterialTaskSerializer(data = data)
        
        already_in_db = MaterialTask.objects.filter(_task = data['_task'], _classroom = data['_classroom'])
                
        if already_in_db:
            serializer = MaterialTaskSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)
        
        return JsonResponse(serializer.data, status = 201)
    
@csrf_exempt
def MaterialTaskViewID(request, _id):

    try: 
        item = MaterialTask.objects.get(_id = _id)
    except MaterialTask.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = MaterialTaskSerializer(item)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = MaterialTaskSerializer(item)
        
        if not('_task' in data):
            data['_task'] = item_serializer.data['_task']

        if not('_classroom' in data):
            data['_classroom'] = item_serializer.data['_classroom']
        
        already_in_db = MaterialTask.objects.filter(_task = data['_task'], _classroom = data['_classroom'])
 
        if already_in_db:
            serializer = MaterialTaskSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer = MaterialSerializer(item, data = data)
            serializer.save()
        else:
            return HttpResponse(status = 400)
        
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

# ********************************
# *     MATERIAL TASK DETAIL     *
# ********************************

@csrf_exempt
def MaterialTaskDetailView(request):
    
    if request.method == 'GET':
        materials = MaterialTaskDetail.objects.all().order_by('_id')
        serializer = MaterialTaskDetailSerializer(materials, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MaterialTaskDetailSerializer(data = data)
        
        already_in_db = MaterialTaskDetail.objects.filter(_material_task = data['_material_task'], _material = data['_material'], _task_quantity = data['_task_quantity'])
                
        if already_in_db:
            serializer = MaterialTaskDetailSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)
        
        return JsonResponse(serializer.data, status = 201)
    
@csrf_exempt
def MaterialTaskDetailViewID(request, _id):

    try: 
        item = MaterialTaskDetail.objects.get(_id = _id)
    except MaterialTaskDetail.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = MaterialTaskDetailSerializer(item)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = MaterialTaskDetailSerializer(item)
        
        if not('_material_task' in data):
            data['_material_task'] = item_serializer.data['_material_task']

        if not('_material' in data):
            data['_material'] = item_serializer.data['_material']
        
        if not('_task_quantity' in data):
            data['_task_quantity'] = item_serializer.data['_task_quantity']
        
        already_in_db = MaterialTaskDetail.objects.filter(_task = data['_task'], _material = data['_material'], _task_quantity = data['_task_quantity'])
 
        if already_in_db:
            serializer = MaterialTaskDetailSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer = MaterialSerializer(item, data = data)
            serializer.save()
        else:
            return HttpResponse(status = 400)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)