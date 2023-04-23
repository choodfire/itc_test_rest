from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('address/', views.AddressView.as_view({'get': 'list'}), name='address'),
    path('university/', views.UniversityView.as_view({'get': 'list'}), name='university'),
    path('department/', views.DepartmentView.as_view({'get': 'list'}), name='department'),
    path('lecturer/', views.LecturerView.as_view({'get': 'list'}), name='lecturer'),
]
