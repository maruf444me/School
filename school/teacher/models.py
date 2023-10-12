from django.db import models



# Models for Add Student Informations
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    cgpa = models.FloatField()