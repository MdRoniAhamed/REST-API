from django.shortcuts import render
# from rest_framework.decorators import APIView 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status

class product_api(APIView):
    def get(self, request, pk = None, format=None):
        if pk:
            pro = Product.objects.get(pk=pk)
            serializer = ProductSerializer(pro)
            return Response(serializer.data)
        pro = Product.objects.all()
        serializer = ProductSerializer(pro, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data has created!!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk=None, format=None):
        pro = Product.objects.get(pk=pk)
        serializer = ProductSerializer(pro,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data has been Updated!!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def patch(self, request,pk=None, format=None):
        pro = Product.objects.get(pk=pk)
        serializer = ProductSerializer(pro,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data has been Updated!!'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None, format=None):
        pro = Product.objects.get(pk=pk)
        name = pro.name
        pro.delete()
        return Response({'msg':f'{name} deleted successful!'})