from django.shortcuts import render 
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        print("*************List***********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ",self.name)
        print("Description: ", self.description)
        pro = Product.objects.all()
        serializer = ProductSerializer(pro, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        print("*************List***********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ",self.name)
        print("Description: ", self.description)
        if pk:
            pro = Product.objects.get(pk=pk)
            serializer = ProductSerializer(pro)
            print("\n Product Nme: ",serializer.data['name'])
            return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Created!'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        pro = Product.objects.get(pk=pk)
        serializer = ProductSerializer(pro, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated successfully!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        pro = Product.objects.get(pk=pk)
        serializer = ProductSerializer(pro, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial updated successfully!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        pro = Product.objects.get(pk=pk)
        pro.delete()
        return Response({'msg':'Data Deleted Successful!'})
        
        
    

