from rest_framework import serializers
from restapp10.models import Manager

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
       model = Manager
       fields = '__all__'


