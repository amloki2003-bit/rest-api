from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=20)
    mail = serializers.EmailField(max_length=30)
    age = serializers.IntegerField()

