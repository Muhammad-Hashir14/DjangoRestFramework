from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from employees.models import Employees
from students.models import Students
from .serializers import EmployeeSerializer
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from staff.models import Staff
from .serializers import StaffSerializer
from rest_framework import generics
from rest_framework import viewsets
from blogs.models import Blogs, Comments
from blogs.serializers import BlogsSerializer, CommentSerializer
from .pagination import CustomPagination
from blogs.filters import BlogsFilters
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.
@api_view(["GET","POST"])
def employees(request):

    # manual serilization
    # employees = Employees.objects.all()
    # employeeslist = list(employees.values())
    # return JsonResponse(employeeslist, safe=False)
    
    if request.method == "GET":
        employees = Employees.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT","DELETE"])
def getEmployee(request, pk):
    
    try:
        employee = Employees.objects.get(pk=pk)
    except Employees.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = EmployeeSerializer(employee,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)  
    
    elif request.method == "DELETE":
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

class Student(APIView):
    def get(self, request):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)

class getStudent(APIView):
    def get_student(self,pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        serializer = StudentSerializer(self.get_student(pk))
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):
        student = self.get_student(pk)
        serializer = StudentSerializer(student, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)

    def delete(self,request, pk):
        student = self.get_student(pk)
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)  

"""
mixins
class StaffView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = Staff.objects.all()
    serializer_class = StaffSerialier
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class getStaff(mixins.UpdateModelMixin, mixins.RetrieveModelMixin ,mixins.DestroyModelMixin, generics.GenericAPIView):
    
    queryset = Staff.objects.all()
    serializer_class = StaffSerialier
    
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
"""

"""
generics
class StaffView(generics.ListCreateAPIView):
    
    queryset = Staff.objects.all()
    serializer_class = StaffSerialier
    
class getStaff(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Staff.objects.all()
    serializer_class = StaffSerialier
    lookup_field = "pk"
"""

"""
viewset
class StaffView(viewsets.ViewSet):
    def list(self, request):
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StaffSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):  
        staff = get_object_or_404(Staff, pk=pk)
        serializer = StaffSerializer(staff)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        staff = get_object_or_404(Staff, pk=pk)
        serializer = StaffSerializer(staff, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None):
        staff = get_object_or_404(Staff, pk=pk)
        staff.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
"""

class StaffView(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer     
    pagination_class = CustomPagination
    filterset_fields = ['staff_designation']
        

# blogs

class BlogsView(generics.ListCreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    filterset_class = BlogsFilters
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_title','blog_content']
    ordering_fields = ['id']
    
class CommentView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    
class getBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    lookup_field="pk"
    
class getComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "pk"