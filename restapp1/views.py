from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapp1.serializer import EmployeeSerializer
from restapp1.models import Employee

# Create your views here.

class EmployeeView(APIView):
    def get(self,request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        pass


