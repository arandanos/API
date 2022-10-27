from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AccesibleElement, DishType
from .serializers import AccesibleElementSerializer, DishTypeSerializer

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