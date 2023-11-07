from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets 

class ProductReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer