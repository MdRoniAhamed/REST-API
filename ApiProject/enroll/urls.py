from django.urls import path, include

urlpatterns = [
    path('',include('enroll.api.urls')),
]
