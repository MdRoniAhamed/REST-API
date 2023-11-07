from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework import viewsets 
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser]
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
