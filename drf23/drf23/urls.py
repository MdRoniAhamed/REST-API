
from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_api/',views.product_api),
    path('product_api/<int:pk>/',views.product_api),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
]
