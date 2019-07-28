from django.shortcuts import render, get_object_or_404
import requests
import json
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department, Employee
from .serializers import EmpSerialiser, DepSerialiser


# Create your views here.

class DepartmentList(ListCreateAPIView):

    serializer_class = DepSerialiser

    def get_queryset(self, *args, **kwargs):
        queryset = Department.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)


class EmployeeList(ListCreateAPIView):

    serializer_class = EmpSerialiser

    def get_queryset(self, *args, **kwargs):
        queryset = Employee.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
