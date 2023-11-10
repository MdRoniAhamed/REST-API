from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView,ListCreateAPIView
from .serializers import StudentSerializer
from .models  import Student


class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer