from rest_framework import serializers
from restapp5.models import Trainer

class TrainerSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

    