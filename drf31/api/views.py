from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle 
from .throttling import JackRateThrottle

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [JackRateThrottle, AnonRateThrottle,UserRateThrottle]
    
