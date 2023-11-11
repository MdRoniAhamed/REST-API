from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()

router.register('singer',views.SingerViewSet, basename='singer')
router.register('song',views.SongViewSet, basename='song')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
]
