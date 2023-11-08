from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from .custom_auth import CustomAuthentication

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    
