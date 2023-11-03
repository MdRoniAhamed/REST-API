from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET','POST','PUT','DELETE','PATCH'])
def product_api(request):
    if request.method == "GET":
        id = request.data.get('id')
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
            return Response({'msg':'Created!'})
        return Response(serializer.errors)
    
    if request.method == "PUT":
        id = request.data['id']
        pro = Product.objects.get(id=id)
        serializer = ProductSerializer(pro,data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Product data Updated'})
        return Response(serializer.errors)
    

    if request.method == "PATCH":
        id = request.data['id']
        pro = Product.objects.get(id=id)
        serializer = ProductSerializer(pro,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Product data Updated'})
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        id = request.data['id']
        pro = Product.objects.get(pk=id)
        pro.delete()
        return Response({'msg':'One item deleted successful!'})