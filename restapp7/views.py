from django.shortcuts import render
from restapp7.models import Customer
from restapp7.serializer import CustomerSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


# Create your views here.
# class CustomerCreateView(GenericAPIView,CreateModelMixin):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
    
# class CustomerListView(GenericAPIView,ListModelMixin):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
# class CustomerRetriveView(GenericAPIView,RetrieveModelMixin):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
# class CustomerUpdateView(GenericAPIView,UpdateModelMixin):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    

# class CustomerDestraoyView(GenericAPIView,DestroyModelMixin):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)
    


class CustomerListCreateView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class CustomerRetrieveUpdateDestraoyView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

