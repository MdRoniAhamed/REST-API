from django.shortcuts import render 
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework import viewsets 
from rest_framework.response import Response

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer