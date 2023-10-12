from django.contrib import admin
from .models import StudentInfo

# Register StudentInfo Models
@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['student_first_name','student_last_name','student_image','student_roll','student_registration','student_age','student_city','student_full_address']
