from django.shortcuts import render
from restapp12.serializer import StudentSerializer
from restapp12.models import Student
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(saddress='sr nagar')
    serializer_class = StudentSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(trainedby=user)

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['saddress','trainedby']

    # filter_backends = [SearchFilter]
    # search_fields = ['saddress']

    filter_backends = [OrderingFilter]
    ordering_fields = ['name']
    








    
    





