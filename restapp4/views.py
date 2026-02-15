from django.shortcuts import render
from restapp4.models import Employee
from restapp4.serializer import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import io


# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeView(View):
    def get(self,request,*args,**kwargs):
        if request.method == 'GET':
            jsondata = request.body
            stream = io.BytesIO(jsondata)
            py_data = JSONParser().parse(stream)
            id = py_data.get('id', None)
            if id is not None:
                emp = Employee.objects.get(id=id)
                serializer = EmployeeSerializer(emp)
                jsondata = JSONRenderer().render(serializer.data)
                return HttpResponse(jsondata, content_type='application/json')
            emp = Employee.objects.all()
            serializer = EmployeeSerializer(emp, many=True)
            jsondata = JSONRenderer().render(serializer.data)
            return HttpResponse(jsondata, content_type='application/json')
        
    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            jsondata = request.body
            stream = io.BytesIO(jsondata)
            py_data = JSONParser().parse(stream)
            serializer = EmployeeSerializer(data=py_data)
            if serializer.is_valid():
                serializer.save()
                result = {'message': 'Data inserted  into database'}
                jsondata = JSONRenderer().render(result)
                return HttpResponse(jsondata, content_type='application/json')
            jsondata = JSONRenderer().render(serializer.errors)
            return HttpResponse(jsondata, content_type='application/json')
        
    def put(self,request,*args,**kwargs):
        if request.method == 'PUT':
            jsondata = request.body
            stream = io.BytesIO(jsondata)
            py_data = JSONParser().parse(stream)
            id = py_data.get('id')
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp, data=py_data)
            if serializer.is_valid():
                serializer.save()
                result = {'message': 'Data updated  into database'}
                jsondata = JSONRenderer().render(result)
                return HttpResponse(jsondata, content_type='application/json')
            jsondata = JSONRenderer().render(serializer.errors)
            return HttpResponse(jsondata, content_type='application/json')
        
    def delete(self,request,*args,**kwargs):
        if request.method == 'DELETE':
            jsondata = request.body
            stream = io.BytesIO(jsondata)
            py_data = JSONParser().parse(stream)
            id = py_data.get('id')
            emp = Employee.objects.get(id=id)
            emp.delete()
            result = {'message': 'Data deleted  from database'}
            jsondata = JSONRenderer().render(result)
            return HttpResponse(jsondata, content_type='application/json')







