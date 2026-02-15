from django.shortcuts import render
from restapp11.models import Manager
from restapp11.serializer import ManagerSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ManagerModelViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]