from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AccesibleElement
from .serializers import AccesibleElementSerializer

# Create your views here.
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