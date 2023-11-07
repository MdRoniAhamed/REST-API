from .serializers import ProductSerializer,Product
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class LCProduct(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class RUDProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
