from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_api/', views.LCProduct.as_view() ),
    path('product_api/<int:pk>/', views.RUDProduct.as_view() ),
]

