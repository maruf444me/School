from django.db import models

# Models for Students
class StudentInfo(models.Model):
    student_first_name = models.CharField(max_length=100)
    student_last_name = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to='students')
    student_roll = models.IntegerField()
    student_registration = models.IntegerField()
    student_age = models.IntegerField()
    student_city = models.CharField(max_length=100)
    student_full_address = models.CharField(max_length=200)

    

