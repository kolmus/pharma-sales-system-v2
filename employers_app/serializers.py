from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import Employee

# TODO => rewrite forms and views
# class EmployeeSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     first_name = serializers.CharField(label='Imię')
#     last_name = serializers.CharField(label='Nazwisko')
#     email = serializers.EmailField(label='Email')
#     phone = serializers.IntegerField(label='Numer telefonu')
#     role = serializers.CharField(label='Stanowisko')
#     supervisor = serializers.ModelChoiceField(queryset=Employee.objects.filter(is_supervisor=True), empty_label='supervisor', label='Przełożony', required=False)





class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'groups', 'is_active']
        
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']