from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = University
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    university = UniversitySerializer()
    employees_number = serializers.ReadOnlyField(source='get_number')

    class Meta:
        model = Department
        fields = '__all__'


class LecturerSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Lecturer
        fields = '__all__'
