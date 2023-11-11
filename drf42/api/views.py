from .serializers import StudentSerializer, Student
from rest_framework.viewsets import ModelViewSet

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
