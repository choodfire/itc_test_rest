import django_filters
from django_filters import FilterSet
from .models import Lecturer


class LecturerFilter(FilterSet):
    first_name = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    middle_name = django_filters.CharFilter(field_name='middle_name', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains')

    class Meta:
        model = Lecturer
        fields = ['first_name', 'middle_name', 'last_name']
