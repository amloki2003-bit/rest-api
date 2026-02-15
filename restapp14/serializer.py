from rest_framework import serializers
from restapp14.models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields=['id','url','name','sid','saddress','mail','age']
