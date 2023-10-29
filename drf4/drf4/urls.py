from django.contrib import admin
from api import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/',views.StudentApi.as_view()),
]
