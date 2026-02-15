from rest_framework import serializers
from restapp4.models import Employee

# class EmployeeSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=20)
#     address=serializers.CharField(max_length=20)
#     mail=serializers.EmailField(max_length=30)
#     age=serializers.IntegerField()

#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.address = validated_data.get('address', instance.address)
#         instance.mail = validated_data.get('mail', instance.mail)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance

def starts_with_s(name):
    if name[0].lower() != 's':
        raise serializers.ValidationError("name should starts with letter s")

class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators = [starts_with_s])
    class Meta:
        model = Employee
        fields = '__all__'
    
    #field level validation
    def validate_age(self,age):
        if age > 100:
            raise serializers.ValidationError("age should not exceed 100")
        return age
    
    #object level validation
    def validate(self,data):
        name = data.get('name')
        addr = data.get('address')
        if name.lower() == 'durga' and addr.lower() !='hyd':
            raise serializers.ValidationError("address must be hyd")
        return data
    

    




        