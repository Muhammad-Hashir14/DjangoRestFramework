from django.shortcuts import render
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
    
            
        
