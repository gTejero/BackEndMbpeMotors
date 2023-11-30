from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework import viewsets
from .serializer import *

class CarrosViewSet(viewsets.ModelViewSet):
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    
