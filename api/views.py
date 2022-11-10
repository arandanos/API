import json
from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AccessibleElement, DishType, Dish, Classroom, Feedback, KitchenOrderDetail, Task, KitchenOrder
from .serializers import AccessibleElementSerializer, DishTypeSerializer, DishSerializer, ClassroomSerializer, FeedbackSerializer, TaskSerializer, KitchenOrderSerializer, KitchenOrderDetailSerializer

# ******************************
# *     ACCESSIBLE ELEMENT     *
# ******************************

#· MÉTODOS AUXILIARES
# Devuelve todos los Elementos accessibles de la tabla de la DB
def getAllAccessibleElements():
    return AccessibleElement.objects.all().order_by('_id').values()

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
        accessible_elements = getAllAccessibleElements()
        serializer = AccessibleElementSerializer(accessible_elements, many = True)
        data = {
            'accessible_elements': serializer.data
        }
        return JsonResponse(data, safe = False)
    
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
        dish_types = DishType.objects.all().order_by('_id').values()
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
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)
        
    
    return HttpResponse(status = 400)

# ******************************
# *            DISH            *
# ******************************

def concatDishWithAccessibleElem(item):
    accessibleElement = getAccessibleElementByID(item['_name'])
    data = {
        "_id": item['_id'],
        "_type": item['_type'],
        "_accessible_element": accessibleElement
    }
    return data

@csrf_exempt
def DishView(request):
    if request.method == 'GET':
        dishes = Dish.objects.all().order_by('_id')
        serializer = DishSerializer(dishes, many = True)

        data = []

        for dish in serializer.data:
            data.append(concatDishWithAccessibleElem(dish))

        return JsonResponse(data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DishSerializer(data = data)
        
        already_in_db = Dish.objects.filter(_name = data['_name'], _type = data['_type'])
                
        if already_in_db:
            serializer = DishSerializer(already_in_db[0])
            return JsonResponse(serializer.data, status = 201)
        elif serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)
    
@csrf_exempt
def DishViewID(request, _id):

    try: 
        item = Dish.objects.get(_id = _id)

    except Dish.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = DishSerializer(item)
        data = concatDishWithAccessibleElem(serializer.data)
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

def concatClassWithAccessibleElem(item):
    accessibleElement = getAccessibleElementByID(item['_class_code'])
    data = {
        "_id": item['_id'],
        "_accessible_element": accessibleElement
    }
    return data

@csrf_exempt
def ClassroomView(request):
    if request.method == 'GET':
        classrooms = Classroom.objects.all().order_by('_id')
        serializer = ClassroomSerializer(classrooms, many = True)

        data = []

        for classroom in serializer.data:
            data.append(concatClassWithAccessibleElem(classroom))

        return JsonResponse(data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClassroomSerializer(data = data)
        
        already_in_db = Classroom.objects.filter(_class_code = data['_class_code'])
                
        if already_in_db:
            serializer = ClassroomSerializer(already_in_db[0])
            return JsonResponse(serializer.data, status = 201)
        elif serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def ClassroomViewID(request, _id):

    try: 
        item = Classroom.objects.get(_id = _id)

    except Classroom.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = ClassroomSerializer(item)
        data = concatClassWithAccessibleElem(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = ClassroomSerializer(item)
        
        if not('_class_code' in data):
            data['_class_code'] = item_serializer.data['_class_code']
        
        already_in_db = Classroom.objects.filter(_class_code = data['_class_code'])
 
        if already_in_db:
            serializer = ClassroomSerializer(already_in_db[0])
            return JsonResponse(serializer.data, safe = False)
        else:
            serializer = ClassroomSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        
        return HttpResponse(status = 400)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)

# ****************************
# *         FEEDBACK         *
# ****************************

@csrf_exempt
def FeedbackView(request):
    if request.method == 'GET':
        feedbacks = Feedback.objects.all().order_by('_id').values()
        serializer = FeedbackSerializer(feedbacks, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedbackSerializer(data = data)
        
        already_in_db = Feedback.objects.filter(_feedback = data['_feedback'])
                
        if already_in_db:
            serializer = FeedbackSerializer(already_in_db[0])
            return JsonResponse(serializer.data, status = 201)
        elif serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)
    
# ****************************
# *           TASK           *
# ****************************

def concatTaskWithAccessibleElem(item):
    accessibleElement = getAccessibleElementByID(item['_name'])
    data = {
        "_id": item['_id'],
        "_due_date": item['_due_date'],
        "_feedback": item['_feedback'],
        "_accessible_element": accessibleElement
    }
    return data

@csrf_exempt
def TaskView(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('_id')
        serializer = TaskSerializer(tasks, many = True)

        data = []

        for task in serializer.data:
            data.append(concatTaskWithAccessibleElem(task))
        return JsonResponse(data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data = data)
        

        already_in_db = Task.objects.filter(_name = data['_name'], _due_date = data['_due_date'])
                
        if 'feedback' in data:
            already_in_db = Task.objects.filter(_name = data['_name'], _due_date = data['_due_date'], _feedback = data['_feedback'])
     
            
        if already_in_db:
            serializer = TaskSerializer(already_in_db[0])
            return JsonResponse(serializer.data, status = 201)
        elif serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)
    
@csrf_exempt
def TaskViewID(request, _id):

    try: 
        item = Task.objects.get(_id = _id)

    except Task.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = TaskSerializer(item)
        data = concatTaskWithAccessibleElem(serializer.data)
        return JsonResponse(data, safe = False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = TaskSerializer(item)
        
        if not('_name' in data):
            data['_name'] = item_serializer.data['_name']
            
        if not('_due_date' in data):
            data['_due_date'] = item_serializer.data['_due_date']
            
        if not('_feedback' in data):
            data['_feedback'] = item_serializer.data['_feedback']
        
        if not('_type' in data):
            data['_type'] = item_serializer.data['_type']
        
        if not('_status' in data):
            data['_status'] = item_serializer.data['_status']
        
        already_in_db = Task.objects.filter(_name = data['_name'], _due_date = data['_due_date'], _feedback = data['_feedback'], _type = data['_type'], _status = data['_status'])
 
        if already_in_db:
            serializer = TaskSerializer(already_in_db[0])
            return JsonResponse(serializer.data, safe = False)
        else:
            serializer = TaskSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        
        return HttpResponse(status = 400)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)
    
# ***************************
# *      KITCHEN ORDER      *
# ***************************

@csrf_exempt
def KitchenOrderView(request):
    
    if request.method == 'GET':
        kitchen_orders = KitchenOrder.objects.all().order_by('_id').values()
        serializer = KitchenOrderSerializer(kitchen_orders, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = KitchenOrderSerializer(data = data)
        
        already_in_db = KitchenOrder.objects.filter(_task = data['_task'])
                
        if already_in_db:
            serializer = KitchenOrderSerializer(already_in_db[0])
            return JsonResponse(serializer.data, status = 201)
        elif serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)
    
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
        kitchen_orders_deatils = KitchenOrderDetail.objects.all().order_by('_id').values()
        serializer = KitchenOrderDetailSerializer(kitchen_orders_deatils, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = KitchenOrderDetailSerializer(data = data)
        
        already_in_db = KitchenOrderDetail.objects.filter(_classroom = data['_classroom'], _dish = data['_dish'], _quantity = data['_quantity'], _kitchen_order = data['_kitchen_order'])
                
        if already_in_db:
            serializer = KitchenOrderDetailSerializer(already_in_db[0])
            return JsonResponse(serializer.data, status = 201)
        elif serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)

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
            return JsonResponse(serializer.data, safe = False)
        else:
            serializer = KitchenOrderDetailSerializer(item, data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        
        return HttpResponse(status = 400)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)
    