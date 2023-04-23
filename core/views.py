from rest_framework import viewsets
import core.filters
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
    # queryset = Lecturer.objects.all()

    def get_filters(self):
        return core.filters.LecturerFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs
