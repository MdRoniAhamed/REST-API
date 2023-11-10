from .serializers import StudentSerializer, Student
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import  User
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user 
        queryset = Student.objects.filter(passby=user)
        return queryset