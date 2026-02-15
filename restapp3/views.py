from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from restapp3.serializer import ManagerSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from restapp3.models import Manager

# Create your views here.

@csrf_exempt
def manager_view(request):
    if request.method == 'POST':
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        py_data = JSONParser().parse(stream)
        serializer = ManagerSerializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            result = {'message':'Manager record inserted'}
            jsondata = JSONRenderer().render(result)
            return HttpResponse(jsondata,content_type = 'application/json')
        jsondata = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')
    

    if request.method == 'PUT':
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        mg = Manager.objects.get(id = id)
        serializer = ManagerSerializer(mg,data=py_data)
        if serializer.is_valid():
            serializer.save()
            result = {'message':'Manager record updated'}
            jsondata = JSONRenderer().render(result)
            return HttpResponse(jsondata,content_type = 'application/json')
        jsondata = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')
    
    if request.method == 'DELETE':
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        mg = Manager.objects.get(id = id)
        mg.delete()
        result = {'message':'Manager record deleted'}
        jsondata = JSONRenderer().render(result)
        return HttpResponse(jsondata,content_type = 'application/json')
    
    if request.method == 'GET':
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id',None)
        if id is not None:
            mg = Manager.objects.get(id=id)
            serializer = ManagerSerializer(mg)
            jsondata = JSONRenderer().render(serializer.data)
            return HttpResponse(jsondata,content_type = 'application/json')
        mg = Manager.objects.all()
        serializer = ManagerSerializer(mg,many = True)
        jsondata = JSONRenderer().render(serializer.data)
        return HttpResponse(jsondata,content_type = 'application/json')



        



        