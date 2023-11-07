from rest_framework import status, viewsets
from .serializers import Course, CourseSerializer
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



# class CourseViewSet(viewsets.ViewSet):
#     def list(self, request):
#         cou = Course.objects.all()
#         serializer = CourseSerializer(cou, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk):
#         cou = Course.objects.get(pk=pk)
#         serializer = CourseSerializer(cou)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'})
#         return Response(serializer.errors)
    
#     def update(self, request, pk):
#         cou = Course.objects.get(pk=pk)
#         serializer = CourseSerializer(cou,request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated!'})
#         return Response(serializer.errors)
        
#     def partial_update(self, request, pk):
#         cou = Course.objects.get(pk=pk)
#         serializer = CourseSerializer(cou,request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated!'})
#         return Response(serializer.errors)

#     def destroy(self, request, pk):
#         cou = Course.objects.get(pk=pk)
#         cou.delete()
#         return Response({'msg':'deleted successfully'})