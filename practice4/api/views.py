from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def product_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id:
            pro = Product.objects.get(pk=id)
            serializer = ProductSerializer(pro)
            return Response(serializer.data,status=status.HTTP_200_OK)
        pro = Product.objects.all()
        serializer = ProductSerializer(pro, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data has Created!!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        pro = Product.objects.get(pk=pk)
        serializer = ProductSerializer(pro, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data has Updated!!'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PATCH":
        pro = Product.objects.get(pk=pk)
        serializer = ProductSerializer(pro, request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data has Updated!!'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        pro = Product.objects.get(pk=pk)
        pro.delete()
        return Response({'msg':'Data has Deleted!!'}) 