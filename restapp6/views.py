from django.shortcuts import render
from restapp6.models import Manager
from restapp6.serailizer import ManagerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class ManagerView(APIView):
    def get(self,request,pk=None):
        id = pk
        if id is not None:
            if Manager.objects.filter(id=id).exists():
               mg = Manager.objects.get(id=id)
               serializer = ManagerSerializer(mg)
               return Response(serializer.data)
            else:
                return Response("id does not exist")
        m = Manager.objects.all()
        serializer = ManagerSerializer(m,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Inserted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        id = pk
        m = Manager.objects.get(pk=id)
        serializer = ManagerSerializer(m,data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response({'message':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,pk):
        id = pk
        m = Manager.objects.get(pk=id) 
        m.delete()
        return Response({'message':'Data Deleted'})



