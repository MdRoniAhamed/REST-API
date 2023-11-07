from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework import viewsets 
from rest_framework.authentication import SessionAuthentication
from .custom_permission import MyPermission

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
   
