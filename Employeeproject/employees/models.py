from django.db import models

# Create your models here.
class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True, auto_created=True)
    employee_name = models.CharField(max_length=30)
    employee_designation = models.CharField(max_length=30)
    employee_salary = models.FloatField()

    def __str__(self):
        return self.employee_name

