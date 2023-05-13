from rest_framework import serializers
from app.models import Employee, User

#class EmployeeSerializer(serializers.Serializer):
    #name=serializers.CharField(max_length=30)
    #email= serializers.EmailField()
    #password=serializers.CharField(max_length=30)
    #phone=serializers.CharField(max_length=10)
    
    #def create(self, validated_data):
    #     print("create method called")
    #     return Employee.objects.create(**validated_data)
    
    # def update(self, employee, validated_data):
    #     newEmployee= Employee(**validated_data)
    #     newEmployee.id=employee.id
    #     newEmployee.save()
    #     return newEmployee
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        #fields=['name', 'email']
        fields='__all__'
        
# class UserSerializer(serializers.Serializer):
#     username=serializers.CharField(max_length=30)
#     email= serializers.EmailField()
#     password=serializers.CharField(max_length=30)
#     first_name=serializers.CharField(max_length=30) 
#     last_name=serializers.CharField(max_length=30)
    
#     def create(self, validated_data):
#         print("created user")
#         return User.objects.create(**validated_data) 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'