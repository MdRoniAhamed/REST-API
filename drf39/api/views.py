from rest_framework.generics import ListCreateAPIView
from .serializers import StudentSerializer
from .models  import Student
from .pagination import MyLimitOffsetPagination

class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyLimitOffsetPagination