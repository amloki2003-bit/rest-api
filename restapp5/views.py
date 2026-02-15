from django.shortcuts import render
from restapp5.serializer import TrainerSerailizer
from restapp5.models import Trainer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def trainer_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            tr=Trainer.objects.get(id=id)
            serializer=TrainerSerailizer(tr)
            return Response(serializer.data)
        tr=Trainer.objects.all()
        serializer=TrainerSerailizer(tr,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=TrainerSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Data inserted"})
        return Response(serializer.errors)
    
    if request.method=='PUT':
        id=request.data.get('id')
        tr=Trainer.objects.get(pk=id)
        serializer=TrainerSerailizer(tr,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Data updated"})
        return Response(serializer.errors)
    
    if request.method=='DELETE':
        id=request.data.get('id')
        tr=Trainer.objects.get(pk=id)
        tr.delete()
        return Response({"message":"Record deleted"})





