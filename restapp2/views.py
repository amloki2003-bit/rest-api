from django.shortcuts import render
from restapp2.models import Employee
from restapp2.serializer import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.

def get_emp_data(request,pk):
    emp = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(emp)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def get_all_emp(self):
    emp = Employee.objects.all()
    serializer = EmployeeSerializer(emp,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


