from rest_framework import serializers
from employees.models import Employees
from students.models import Students
from staff.models import Staff

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"
        
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"
        
        