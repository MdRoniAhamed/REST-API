
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_api/',views.ProductList.as_view()),
    path('product_api/<int:pk>/',views.ProductDestroy.as_view()),
]
