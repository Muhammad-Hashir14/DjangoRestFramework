from django.db import models

# Create your models here.
class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True, auto_created=True)
    staff_name = models.CharField(max_length=30)
    staff_designation = models.CharField(max_length=30)
    staff_courses = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.staff_name}_{self.staff_id}"