from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AccesibleElement
from .serializers import AccesibleElementSerializer

# Create your views here.
@csrf_exempt
def AccesibleElementView(request):
    if request.method == 'GET':
        accesibles_elements = AccesibleElement.objects.all()
        serializer = AccesibleElementSerializer(accesibles_elements, many =True)
        return JsonResponse(serializer.data, safe =False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccesibleElementSerializer(data = data)
        
        accesibles_elements = AccesibleElement.objects.all()
        already_exists = accesibles_elements.filter(_text = data['_text'], _pictogram = data['_pictogram'])
                
        # TODO: Comprobar que no existe otra entrada con los mismos campos _text y _pictogram
        if serializer.is_valid() and not(already_exists):
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)