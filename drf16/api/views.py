from .models import Product 
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class LCProduct(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class RUDProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
