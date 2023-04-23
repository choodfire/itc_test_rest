from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class DepartmentView(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class UniversityView(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()


class LecturerView(viewsets.ModelViewSet):
    serializer_class = LecturerSerializer
    queryset = Lecturer.objects.all()
