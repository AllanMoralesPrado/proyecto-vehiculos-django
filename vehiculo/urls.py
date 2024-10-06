from django.urls import path, include
from .views import (
    AddVehicleView,
)

urlpatterns = [
    path('add/', AddVehicleView.as_view(), name="agregar_vehiculo"),
]
