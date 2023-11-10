from .models import Product 
from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle



class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewpro'

class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifypro'


class ProductUpdate(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifypro'

class ProductRetrieve(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewpro'

class ProductDestroy(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifypro'
