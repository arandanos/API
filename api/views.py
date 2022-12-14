import json
from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from .models import *
from .serializers import  *
from django.conf import settings
from django.http import FileResponse
import validators

# ******************************
# *           IMAGE            *
# ******************************
@csrf_exempt
def ImageViewID(request, _image):
    filename = settings.SAVE_IMAGE_URL + _image
    return FileResponse(open(filename, 'rb'), as_attachment=False)


# ******************************
# *     ACCESSIBLE ELEMENT     *
# ******************************

#· MÉTODOS AUXILIARES
# Devuelve el elemento de la base de datos que corresponda con el id
def getAccessibleElementByID(_id):
    item = AccessibleElement.objects.get(_id = _id)
    serializer = AccessibleElementSerializer(item)
    return serializer.data

def getNewID():
    accessible_elements = AccessibleElement.objects.all().order_by('_id')
    data = AccessibleElementSerializer(accessible_elements, many = True).data
    new_id = 1
    if len(data) != 0:
        new_id = data[len(data) - 1]['_id'] + 1
    return new_id
    
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

        if not validators.url(data['_pictogram']):
            encode_data = base64.b64decode(data['_pictogram'])
            data['_pictogram'] = str(getNewID()) + '.jpg'
            filename = settings.SAVE_IMAGE_URL + data['_pictogram']

            with open(filename, 'wb') as f:
                f.write(encode_data)

        serializer = AccessibleElementSerializer(data = data)
        
        already_in_db = AccessibleElement.objects.filter(_text = data['_text'], _pictogram = data['_pictogram'])
                
        if already_in_db:
            serializer = AccessibleElementSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)
    
        return JsonResponse(serializer.data, status = 201)

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
        else:
            serializer = AccessibleElementSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
            else:
                return HttpResponse(status = 400)
        
        return JsonResponse(serializer.data, safe = False)

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
                return JsonResponse(serializer.data, safe = False)
        
        return HttpResponse(status = 400)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)
        
    
    return HttpResponse(status = 400)

# ******************************
# *            DISH            *
# ******************************

#· MÉTODOS AUXILIARES
def concatenateDish(data):
    data['_name'] = getAccessibleElementByID(data['_name'])
    return data

def getDishByID(_id):
    item = Dish.objects.get(_id = _id)
    serializer = DishSerializer(item)
    data = concatenateDish(serializer.data)
    return data

@csrf_exempt
def DishView(request):
    if request.method == 'GET':
        dishes = Dish.objects.all().order_by('_id')
        serializer = DishSerializer(dishes, many = True)

        for dish in serializer.data:
            dish = concatenateDish(dish)

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
        
        data = concatenateDish(serializer.data)
        return JsonResponse(data, status = 201)
    
@csrf_exempt
def DishViewID(request, _id):

    try: 
        item = Dish.objects.get(_id = _id)
    except Dish.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = DishSerializer(item)
        data = concatenateDish(serializer.data)
        return JsonResponse(data, safe = False)
    
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
        else:
            serializer = DishSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
            else:
                return HttpResponse(status = 400)
        
        data = concatenateDish(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)
    
# *****************************
# *         CLASSROOM         *
# *****************************

#· MÉTODOS AUXILIARES
def concatenateClassroom(data):
    data['_name'] = getAccessibleElementByID(data['_name'])
    return data

def getClassroomByID(_id):
    item = Classroom.objects.get(_id = _id)
    serializer = ClassroomSerializer(item)
    data = concatenateClassroom(serializer.data)
    return data

@csrf_exempt
def ClassroomView(request):
    if request.method == 'GET':
        classrooms = Classroom.objects.all().order_by('_id')
        serializer = ClassroomSerializer(classrooms, many = True)

        for classroom in serializer.data:
            classroom = concatenateClassroom(classroom)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClassroomSerializer(data = data)
        
        already_in_db = Classroom.objects.filter(_name = data['_name'])
                
        if already_in_db:
            serializer = ClassroomSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = concatenateClassroom(serializer.data)
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
        data['_name'] = getAccessibleElementByID(serializer.data['_name'])
        return JsonResponse(data, safe = False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = ClassroomSerializer(item)
        
        if not('_name' in data):
            data['_name'] = item_serializer.data['_name']
        
        already_in_db = Classroom.objects.filter(_name = data['_name'])
 
        if already_in_db:
            serializer = ClassroomSerializer(already_in_db[0])
        else:
            serializer = ClassroomSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
            else:
                return HttpResponse(status = 400)
        
        data = concatenateClassroom(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

# ****************************
# *         FEEDBACK         *
# ****************************

#· MÉTODOS AUXILIARES
def concatenateFeedback(data):
    data['_name'] = getAccessibleElementByID(data['_name'])
    return data

def getFeedbackByID(_id):
    item = Feedback.objects.get(_id = _id)
    serializer = FeedbackSerializer(item)
    data = concatenateFeedback(serializer.data)
    return data

@csrf_exempt
def FeedbackView(request):
    if request.method == 'GET':
        feedbacks = Feedback.objects.all().order_by('_id')
        serializer = FeedbackSerializer(feedbacks, many = True)

        for feedback in serializer.data:
            feedback = concatenateFeedback(feedback)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedbackSerializer(data = data)
        
        already_in_db = Feedback.objects.filter(_feedback = data['_name'])
                
        if already_in_db:
            serializer = FeedbackSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = concatenateFeedback(serializer.data)
        return JsonResponse(data, status = 201)
    
# ****************************
# *           TASK           *
# ****************************

#· MÉTODOS AUXILIARES
def concatenateTask(data):
    data['_name'] = getAccessibleElementByID(data['_name'])

    if '_feedback' in data and not data['_feedback'] == None:
        data['_feedback'] = getFeedbackByID(data['_feedback'])

    return data

def getTaskByID(_id):
    item = Task.objects.get(_id = _id)
    serializer = TaskSerializer(item)
    data = concatenateTask(serializer.data)
    return data

@csrf_exempt
def TaskView(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('_id')
        serializer = TaskSerializer(tasks, many = True)

        for task in serializer.data:
            task = concatenateTask(task)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data = data)

        already_in_db = Task.objects.filter(_name = data['_name'], _due_date = data['_due_date'])
                
        if not data['_feedback'] == None:
            already_in_db = Task.objects.filter(_name = data['_name'], _due_date = data['_due_date'], _feedback = data['_feedback'])

        if already_in_db:
            serializer = TaskSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = concatenateTask(serializer.data)
        return JsonResponse(data, status = 201)
    
@csrf_exempt
def TaskViewID(request, _id):

    try: 
        item = Task.objects.get(_id = _id)
    except Task.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = TaskSerializer(item)
        data = concatenateTask(serializer.data)
        return JsonResponse(data, safe = False)
    
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
        else:
            serializer = TaskSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
            else:
                return HttpResponse(status = 400)

        data = concatenateTask(serializer.data)
        return JsonResponse(data, safe = False)

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)
    
# ***************************
# *      KITCHEN ORDER      *
# ***************************

#· MÉTODOS AUXILIARES
def concatenateKitchenOrder(data):
    data['_task'] = getTaskByID(data['_task'])
    return data

def getKitchenOrderByID(_id):
    item = KitchenOrder.objects.get(_id = _id)
    serializer = KitchenOrderSerializer(item)
    data = concatenateKitchenOrder(serializer.data)
    return data

@csrf_exempt
def KitchenOrderView(request):
    
    if request.method == 'GET':
        kitchen_orders = KitchenOrder.objects.all().order_by('_id')
        serializer = KitchenOrderSerializer(kitchen_orders, many = True)

        for kitchen_order in serializer.data:
            kitchen_order = concatenateKitchenOrder(kitchen_order)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = KitchenOrderSerializer(data = data)
        
        already_in_db = KitchenOrder.objects.filter(_task = data['_task'])
                
        if already_in_db:
            serializer = KitchenOrderSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = concatenateKitchenOrder(serializer.data)
        return JsonResponse(data, status = 201)
    
@csrf_exempt
def KitchenOrderViewID(request, _id):

    try: 
        item = KitchenOrder.objects.get(_id = _id)
    except AccessibleElement.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = KitchenOrderSerializer(item)
        data = concatenateKitchenOrder(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

@csrf_exempt
def KitchenOrderViewTaskID(request, _id):

    try: 
        item = KitchenOrder.objects.get(_task_id = _id)
    except KitchenOrder.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = KitchenOrderSerializer(item)
        data = concatenateKitchenOrder(serializer.data)
        return JsonResponse(data, safe = False)

    return HttpResponse(status = 404)

# ********************************
# *     KITCHEN ORDER DETAIL     *
# ********************************

#· MÉTODOS AUXILIARES
def concatenateKitchenOrderDetail(data):
    data['_classroom'] = getClassroomByID(data['_classroom'])
    data['_dish'] = getDishByID(data['_dish'])
    data['_kitchen_order'] = getKitchenOrderByID(data['_kitchen_order'])
    return data

@csrf_exempt
def KitchenOrderDetailView(request):
    
    if request.method == 'GET':
        kitchen_orders_deatils = KitchenOrderDetail.objects.all().order_by('_id')
        serializer = KitchenOrderDetailSerializer(kitchen_orders_deatils, many = True)

        for kitchen_order_detail in serializer.data:
            kitchen_order_detail = concatenateKitchenOrderDetail(kitchen_order_detail)

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

        data = concatenateKitchenOrderDetail(serializer.data)
        return JsonResponse(data, status = 201)

@csrf_exempt
def KitchenOrderDetailViewID(request, _id):

    try: 
        item = KitchenOrderDetail.objects.get(_id = _id)
    except KitchenOrderDetail.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = KitchenOrderDetailSerializer(item).data
        data = concatenateKitchenOrderDetail(serializer.data)
        return JsonResponse(data, safe = False)
    
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
        else:
            serializer = KitchenOrderDetailSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
            else:
                return HttpResponse(status = 400)
        
        data = concatenateKitchenOrderDetail(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

@csrf_exempt
def KitchenOrderDetailViewClassOrder(request, _classroom, _kitchen_order):
    if request.method == 'GET':
        item = KitchenOrderDetail.objects.filter(_classroom_id = _classroom, _kitchen_order_id = _kitchen_order).order_by('_id')
        serializer = KitchenOrderDetailSerializer(item, many = True)

        for kitchen_order_detail in serializer.data:
            kitchen_order_detail = concatenateKitchenOrderDetail(kitchen_order_detail)

        return JsonResponse(serializer.data, safe = False)

    return HttpResponse(status = 404)


# *****************************
# *       MATERIAL TYPE       *
# *****************************

#· MÉTODOS AUXILIARES
def concatenateMaterialType(data):
    data['_name'] = getAccessibleElementByID(data['_name'])
    return data

def getMaterialTypeByID(_id):
    item = MaterialType.objects.get(_id = _id)
    serializer = MaterialTypeSerializer(item)
    data = concatenateMaterialType(serializer.data)
    return data

@csrf_exempt
def MaterialTypeView(request):
    if request.method == 'GET':
        material_types = MaterialType.objects.all().order_by('_id')
        serializer = MaterialTypeSerializer(material_types, many = True)

        for material_type in serializer.data:
            material_type = concatenateMaterialType(material_type)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MaterialTypeSerializer(data = data)
        
        already_in_db = MaterialType.objects.filter(_name = data['_name'])
                
        if already_in_db:
            serializer = MaterialTypeSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = concatenateMaterialType(serializer.data)
        return JsonResponse(data, status = 201)

@csrf_exempt
def MaterialTypeViewID(request, _id):

    try: 
        item = MaterialType.objects.get(_id = _id)
    except MaterialType.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = MaterialTypeSerializer(item)
        data = concatenateMaterialType(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

# **************************
# *        MATERIAL        *
# **************************

#· MÉTODOS AUXILIARES
def concatenateMaterial(data):
    data['_color'] = getAccessibleElementByID(data['_color'])
    data['_type'] = getMaterialTypeByID(data['_type'])
    return data

def getMaterialByID(_id):
    item = Material.objects.get(_id = _id)
    serializer = MaterialSerializer(item)
    data = concatenateMaterial(serializer.data)
    return data

@csrf_exempt
def MaterialView(request):
    
    if request.method == 'GET':
        materials = Material.objects.all().order_by('_id')
        serializer = MaterialSerializer(materials, many = True)

        for material in serializer.data:
            material = concatenateMaterial(material)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MaterialSerializer(data = data)
        
        already_in_db = Material.objects.filter(_type = data['_type'], _color = data['_color'], _quantity = data['_quantity'])
                
        if already_in_db:
            serializer = KitchenOrderSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)
        
        data = concatenateMaterial(serializer.data)
        return JsonResponse(data, status = 201)
    
@csrf_exempt
def MaterialViewID(request, _id):

    try: 
        item = Material.objects.get(_id = _id)
    except Material.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = MaterialSerializer(item)
        data = concatenateMaterial(serializer.data)
        return JsonResponse(data, safe = False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = MaterialSerializer(item)
        
        if not('_name' in data):
            data['_name'] = item_serializer.data['_name']

        if not('_color' in data):
            data['_color'] = item_serializer.data['_color']

        if not('_quantity' in data):
            data['_quantity'] = item_serializer.data['_quantity']
        
        already_in_db = Material.objects.filter(_name = data['_name'], _color = data['_color'], _quantity = data['_quantity'])
 
        if already_in_db:
            serializer = MaterialSerializer(already_in_db[0])
        else:
            serializer = MaterialSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
            else:
                return HttpResponse(status = 400)
        
        data = concatenateMaterial(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

@csrf_exempt
def MaterialViewTypeID(request, _id):

    if request.method == 'GET':
        materials = Material.objects.filter(_type = _id)
        serializer = MaterialSerializer(materials, many = True)

        for material in serializer.data:
            material = concatenateMaterial(material)

        return JsonResponse(serializer.data, safe = False)

# ***************************
# *      MATERIAL TASK      *
# ***************************

#· MÉTODOS AUXILIARES
def concatenateMaterialTask(data):
    data['_task'] = getTaskByID(data['_task'])
    data['_classroom'] = getClassroomByID(data['_classroom'])
    return data

def getMaterialTaskByID(_id):
    item = MaterialTask.objects.get(_id = _id)
    serializer = MaterialTaskSerializer(item)
    data = concatenateMaterialTask(serializer.data)
    return data

@csrf_exempt
def MaterialTaskView(request):
    
    if request.method == 'GET':
        materials = MaterialTask.objects.all().order_by('_id')
        serializer = MaterialTaskSerializer(materials, many = True)

        for material in serializer.data:
            material = concatenateMaterialTask(material)

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

        data = concatenateMaterialTask(serializer.data)
        return JsonResponse(data, status = 201)
    
@csrf_exempt
def MaterialTaskViewID(request, _id):

    try: 
        item = MaterialTask.objects.get(_id = _id)
    except MaterialTask.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = MaterialTaskSerializer(item)
        data = concatenateMaterialTask(serializer.data)
        return JsonResponse(data, safe = False)

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
        else:
            serializer = MaterialTaskSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
            else:
                return HttpResponse(status = 400)

        data = concatenateMaterialTask(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

@csrf_exempt
def MaterialTaskViewTaskID(request, _id):

    try: 
        item = MaterialTask.objects.get(_task_id = _id)
    except MaterialTask.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = MaterialTaskSerializer(item)
        data = concatenateMaterialTask(serializer.data)
        return JsonResponse(data, safe = False)

    return HttpResponse(status = 404)

# ********************************
# *     MATERIAL TASK DETAIL     *
# ********************************

#· MÉTODOS AUXILIARES
def concatenateMaterialTaskDetail(data):
    data['_material_task'] = getMaterialTaskByID(data['_material_task'])
    data['_material'] = getMaterialByID(data['_material'])   
    return data

@csrf_exempt
def MaterialTaskDetailView(request):
    
    if request.method == 'GET':
        materials = MaterialTaskDetail.objects.all().order_by('_id')
        serializer = MaterialTaskDetailSerializer(materials, many = True)

        for material_task_detail in serializer.data:
            material_task_detail = concatenateMaterialTaskDetail(material_task_detail)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MaterialTaskDetailSerializer(data = data)
        
        already_in_db = MaterialTaskDetail.objects.filter(_material_task = data['_material_task'], _material = data['_material'], _quantity = data['_quantity'])
                
        if already_in_db:
            serializer = MaterialTaskDetailSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = concatenateMaterialTaskDetail(serializer.data)         
        return JsonResponse(data, status = 201)
    
@csrf_exempt
def MaterialTaskDetailViewID(request, _id):

    try: 
        item = MaterialTaskDetail.objects.get(_id = _id)
    except MaterialTaskDetail.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = MaterialTaskDetailSerializer(item)
        data = concatenateMaterialTaskDetail(serializer.data)  
        return JsonResponse(data, safe = False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = MaterialTaskDetailSerializer(item)
        
        if not('_material_task' in data):
            data['_material_task'] = item_serializer.data['_material_task']

        if not('_material' in data):
            data['_material'] = item_serializer.data['_material']
        
        if not('_quantity' in data):
            data['_quantity'] = item_serializer.data['_quantity']
        
        already_in_db = MaterialTaskDetail.objects.filter(_task = data['_task'], _material = data['_material'], _quantity = data['_quantity'])
 
        if already_in_db:
            serializer = MaterialTaskDetailSerializer(already_in_db[0])
        else:
            serializer = MaterialTaskDetailSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
            else:
                return HttpResponse(status = 400)

        data = concatenateMaterialTaskDetail(serializer.data)  
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

csrf_exempt
def MaterialTaskDetailViewTaskID(request, _id):
    if request.method == 'GET':
        material_task_details = MaterialTaskDetail.objects.filter(_material_task = _id)
        serializers = MaterialTaskDetailSerializer(material_task_details, many = True)

        for material_task_detail in serializers.data:
            material_task_detail = concatenateMaterialTaskDetail(material_task_detail)

        return JsonResponse(serializers.data, safe = False)

    return HttpResponse(status = 400)
# *****************************
# *           COLOR           *
# *****************************

#· MÉTODOS AUXILIARES
def concatenateColor(data):
    data['_name'] = getAccessibleElementByID(data['_name'])
    return data

def getColorByID(_id):
    item = Color.objects.get(_id = _id)
    serializer = ColorSerializer(item)
    data = concatenateColor(serializer.data)
    return data

@csrf_exempt
def ColorView(request):
    if request.method == 'GET':
        colors = Color.objects.all().order_by('_id')
        serializer = ColorSerializer(colors, many = True)

        for color in serializer.data:
            color = concatenateColor(color)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ColorSerializer(data = data)
        
        already_in_db = Color.objects.filter(_name = data['_name'])
                
        if already_in_db:
            serializer = Color(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = concatenateColor(serializer.data)
        return JsonResponse(data, status = 201)

# ************************************
# *      LAMINATOR PRINTER TASK      *
# ************************************

#· MÉTODOS AUXILIARES
def concatenatePrinterLaminatorTask(data):
    data['_task'] = getTaskByID(data['_task'])
    data['_classroom'] = getClassroomByID(data['_classroom'])

    if not data['_color'] == None:
        data['_color'] = getColorByID(data['_color'])

    return data

@csrf_exempt
def PrinterLaminatorTaskView(request):
    
    if request.method == 'GET':
        tasks = PrinterLaminatorTask.objects.all().order_by('_id')
        serializer = PrinterLaminatorTaskSerializer(tasks, many = True)

        for task in serializer.data:
            task = concatenatePrinterLaminatorTask(task)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PrinterLaminatorTaskSerializer(data = data)
        
        already_in_db = PrinterLaminatorTask.objects.filter(_task = data['_task'], _classroom = data['_classroom'])
                
        if already_in_db:
            serializer = PrinterLaminatorTaskSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = concatenatePrinterLaminatorTask(serializer.data)
        return JsonResponse(data, status = 201)
    
@csrf_exempt
def PrinterLaminatorTaskViewID(request, _id):

    try: 
        item = PrinterLaminatorTask.objects.get(_id = _id)
    except AccessibleElement.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = PrinterLaminatorTaskSerializer(item)
        data = concatenatePrinterLaminatorTask(serializer.data)
        return JsonResponse(data, safe = False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = PrinterLaminatorTaskSerializer(item)
        
        if not('_classroom' in data):
            data['_classroom'] = item_serializer.data['_classroom']

        if not('_task' in data):
            data['_task'] = item_serializer.data['_task']
        
        already_in_db = PrinterLaminatorTask.objects.filter(_task = data['_task'], _classroom = data['_classroom'])
 
        if already_in_db:
            serializer = PrinterLaminatorTaskSerializer(already_in_db[0])
        else:
            serializer = PrinterLaminatorTaskSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
            else:
                return HttpResponse(status = 400)

        data = concatenatePrinterLaminatorTask(serializer.data)  
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)


# ***************************
# *         TEACHER         *
# ***************************

def concatenateTeacher(data):
    data['_name'] = getAccessibleElementByID(data['_name'])
    return data

def getTeacherByID(_id):
    item = Teacher.objects.get(_id = _id)
    serializer = TeacherSerializer(item)
    data = concatenateTeacher(serializer.data)
    return data

@csrf_exempt
def TeacherView(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all().order_by('_id')
        serializer = TeacherSerializer(teachers, many = True)

        for teacher in serializer.data:
            teacher = concatenateTeacher(teacher)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Teacher(data = data)
                
        if serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = concatenateTeacher(serializer.data)
        return JsonResponse(data, status = 201)

def TeacherViewID(request, _id):
    try: 
        item =  Teacher.objects.get(_id = _id)
    except Teacher.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = TeacherSerializer(item)
        data = concatenateTeacher(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = TeacherSerializer(item)
        
        if not('_name' in data):
            data['_name'] = item_serializer.data['_name']
            
        if not('_username' in data):
            data['_username'] = item_serializer.data['_username']

        if not('_password' in data):
            data['_password'] = item_serializer.data['_password']

        if not('_admin' in data):
            data['_admin'] = item_serializer.data['_admin']
        
        serializer = AccessibleElementSerializer(item, data = data)

        if serializer.is_valid():
            serializer.save()
        else:
            return HttpResponse(status = 400)
        
        data = concatenateTeacher(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

# ***************************
# *         TEACHES         *
# ***************************

def concatenateTeach(data):
    data['_teacher'] = getTeacherByID(data['_teacher'])
    data['_classroom'] = getClassroomByID(data['_classroom'])
    return data

@csrf_exempt
def TeachView(request):
    if request.method == 'GET':
        teaches = Teach.objects.all().order_by('_id')
        serializer = TeachSerializer(teaches, many = True)

        for teach in serializer.data:
            teach = concatenateTeach(teach)

        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Teach(data = data)

        already_in_db = Teach.objects.filter(_teacher = data['_teacher'], _classroom = data['_classroom'])
 
        if already_in_db:
            serializer = TeachSerializer(already_in_db[0])
        elif serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status = 400)

        data = concatenateTeach(serializer.data)
        return JsonResponse(data, status = 201)

def TeachViewID(request, _id):
    try: 
        item =  Teach.objects.get(_id = _id)
    except Teach.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = TeachSerializer(item)
        data = concatenateTeach(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)