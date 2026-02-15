from rest_framework import serializers
from restapp13.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
       model = Student
       fields = '__all__'


