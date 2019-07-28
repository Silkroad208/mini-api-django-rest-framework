from rest_framework import serializers
from .models import Employee, Department
from rest_framework import viewsets


class DepSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class EmpSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
