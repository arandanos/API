from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AccesibleElement, DishType, Dish, Classroom, Task, KitchenOrder
from .serializers import AccesibleElementSerializer, DishTypeSerializer, DishSerializer, ClassroomSerializer, TaskSerializer, KitchenOrderSerializer

# Create your views here.
# *****************************
# *     ACCESIBLE ELEMENT     *
# *****************************
# Peticiones GET y POST simples
@csrf_exempt
def AccesibleElementView(request):
    # Devuelve todos los elementos de la tabla Accesible_Element
    if request.method == 'GET':
        accesibles_elements = AccesibleElement.objects.all()
        serializer = AccesibleElementSerializer(accesibles_elements, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    # Crea una nueva entrada en la tabla Accesible_Element si no hay ninguno con la misma información
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccesibleElementSerializer(data = data)
        
        already_in_db = AccesibleElement.objects.filter(_text = data['_text'], _pictogram = data['_pictogram'])
                
        if already_in_db:
            serializer = AccesibleElementSerializer(already_in_db[0])
            return JsonResponse(serializer.data, status = 201)
        elif serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)
    
# Peticiones GET y POST pasando una ID como argumento
@csrf_exempt
def AccesibleElementViewID(request, _id):
    # Comprobación de que existe un elemento en la tabla con la ID
    try: 
        item = AccesibleElement.objects.get(_id = _id)
    # Si no existe se lanza un error 404
    except AccesibleElement.DoesNotExist:
        raise Http404('Not found')
    
    # Se devuelve la entrada de la tabla con igual ID
    if request.method == 'GET':
        serializer = AccesibleElementSerializer(item)
        return JsonResponse(serializer.data, safe = False)
    
    # Se modifica la entrada de la tabla con igual ID si no existe otro elemento que tenga la misma informacón tras modificar la entrada
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = AccesibleElementSerializer(item)
        
        if not('_text' in data):
            data['_text'] = item_serializer.data['_text']
            
        if not('_pictogram' in data):
            data['_pictogram'] = item_serializer.data['_pictogram']
        
        # Devuelve un array con todos los objetos cuyos valores sean los mismos que los argumentos
        already_in_db = AccesibleElement.objects.filter(_text = data['_text'], _pictogram = data['_pictogram'])
 
        if already_in_db:
            serializer = AccesibleElementSerializer(already_in_db[0])
            return JsonResponse(serializer.data, safe = False)
        else:
            serializer = AccesibleElementSerializer(item, data = data)
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
        dish_types = DishType.objects.all()
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

@csrf_exempt
def DishView(request):
    if request.method == 'GET':
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many = True)
        return JsonResponse(serializer.data, safe = False)
    
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
        return True

    if request.method == 'GET':
        serializer = DishSerializer(item)
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
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many = True)
        return JsonResponse(serializer.data, safe = False)
    
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
        return True

    if request.method == 'GET':
        serializer = ClassroomSerializer(item)
        return JsonResponse(serializer.data, safe = False)
    
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
# *           TASK           *
# ****************************

@csrf_exempt
def TaskView(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data = data)
        
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
        return True

    if request.method == 'GET':
        serializer = TaskSerializer(item)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        item_serializer = TaskSerializer(item)
        
        if not('_name' in data):
            data['_name'] = item_serializer.data['_name']
            
        if not('_due_date' in data):
            data['_due_date'] = item_serializer.data['_due_date']
            
        if not('_feedback' in data):
            data['_feedback'] = item_serializer.data['_feedback']
        
        already_in_db = Task.objects.filter(_name = data['_name'], _due_date = data['_due_date'], _feedback = data['_feedback'])
 
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
        kitchen_orders = KitchenOrder.objects.all()
        serializer = KitchenOrderSerializer(kitchen_orders, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = KitchenOrderSerializer(data = data)
        
        already_in_db = KitchenOrder.objects.filter(_id = data['_id'])
                
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
    except AccesibleElement.DoesNotExist:
        raise Http404('Not found')
    
    if request.method == 'GET':
        serializer = KitchenOrderSerializer(item)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status = 204)