from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET','POST','PUT','DELETE','PATCH'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def product_api(request,pk=None):
    if request.method == "GET":
        id = pk
        if id:
            pro = Product.objects.get(id=id)
            serializer = ProductSerializer(pro)
            return Response(serializer.data)
        pro = Product.objects.all()
        serializer = ProductSerializer(pro,many=True)
        return Response(serializer.data)

    if request.method == "POST":

        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Created!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PUT":
        id = pk
        pro = Product.objects.get(id=id)
        serializer = ProductSerializer(pro,data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == "PATCH":
        id = pk
        pro = Product.objects.get(id=id)
        serializer = ProductSerializer(pro,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        id = pk
        pro = Product.objects.get(pk=id)
        pro.delete()
        return Response({'msg':'One item deleted successful!'})