
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Create Router Object
router = DefaultRouter()

# Register Router with ViewSet Class
router.register('product_api',views.ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]
