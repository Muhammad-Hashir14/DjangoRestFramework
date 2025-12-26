from django.db import models

# Create your models here.

class Students(models.Model):
    student_id = models.IntegerField(primary_key=True, auto_created=True)
    student_name = models.CharField(max_length=30)
    student_department = models.CharField(max_length = 30)
    student_course = models.CharField(max_length= 30)
    
    def __str__(self):
        return self.student_name
    