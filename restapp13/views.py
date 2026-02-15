from django.shortcuts import render
from restapp13.models import Student
from restapp13.serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from restapp13.pagination import MyPagination
# Create your views here.

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPagination


