from django.shortcuts import render
from restapp9.models import Customer
from restapp9.serializer import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
# class CustomverViewSet(viewsets.ViewSet):
#     def list(self,request):
#         customer = Customer.objects.all()
#         serializer = CustomerSerializer(customer,many = True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         id = pk
#         if id is not None:
#             customer  = Customer.objects.get(id=id)
#             serializer = CustomerSerializer(customer)
#             return Response(serializer.data)
        
#     def create(self, request):
#         serializer = CustomerSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'Data Inserted'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def update(self,request,pk):
#         id = pk
#         customer = Customer.objects.get(pk=id)
#         serializer = CustomerSerializer(customer,data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'Data Updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#     def delete(self,request,pk):
#         id = pk
#         customer = Customer.objects.get(pk=id)
#         customer.delete()
#         return Response({'message':'Data Deleted'})


# class CustomverViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer


class CustomverViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer




