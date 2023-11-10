from rest_framework.generics import ListCreateAPIView
from .serializers import StudentSerializer
from .models  import Student
from .pagination import MyPageNumberPagination

class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination