from django.shortcuts import render
from .models import StudentInfo


# Function for Student home page
def student_home(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_image = request.FILES.get('image')
        student_roll = request.POST.get('roll')
        student_registration = request.POST.get('registration')
        student_age = request.POST.get('age')
        student_city = request.POST.get('city')
        student_full_address = request.POST.get('address')

        # Create and save the StudentInfo object inside the POST block
        stuinfo = StudentInfo(
            student_first_name=first_name,
            student_last_name=last_name,
            student_image=student_image,
            student_roll=student_roll,
            student_registration=student_registration,
            student_age=student_age,
            student_city=student_city,
            student_full_address=student_full_address
        )
        stuinfo.save()

    return render(request, 'student/student_home.html')
