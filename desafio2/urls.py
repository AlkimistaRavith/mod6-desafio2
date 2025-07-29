from django.urls import path
from desafio2 import views

urlpatterns = [
    path("empleados/", views.empleados, name="empleados"),
]