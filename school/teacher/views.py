from django.shortcuts import render, redirect
from .models import Student




# Student Home Page
def teacher_home(request):
    return render(request, 'teacher/teacher_home.html')


# Add Student
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        city = request.POST.get('city')
        cgpa = request.POST.get('cgpa')

        if not is_valid_student_data(name, roll, city, cgpa):
            return render(request, 'teacher/add_student.html', {'error_message': 'Input Valid Value'})

        student_info = Student(
            name = name,
            roll = roll,
            city = city,
            cgpa = cgpa
        )
        student_info.save()
        return redirect('/teacher/show_student/')
    return render(request, 'teacher/add_student.html')

# Custom Validations
def is_valid_student_data(name, roll, city, cgpa):
    if not name or not roll or not city or not cgpa:
        return False
    try:
        cgpa = float(cgpa)
        if cgpa < 0 or cgpa > 5.0:
            return False
    except ValueError:
        return False
    return True


# Show Student
def show_student(request):
    stu_info = Student.objects.all()    
    return render(request, 'teacher/show_student.html', {'stu_info': stu_info})


# Update Student Data
def update_data(request,id):
    student = Student.objects.get(pk=id)
    
    if request.method == 'POST':
        data = request.POST
        new_name = data.get('name')
        new_roll = data.get('roll')
        new_city = data.get('city')
        new_cgpa = data.get('cgpa')

        student.name = new_name
        student.roll = new_roll
        student.city = new_city
        student.cgpa = new_cgpa
        student.save()
        return redirect('/teacher/show_student')
    return render(request, 'teacher/update_student.html', {'stu_info': student})



# Delete Data
def delete_data(request, id):
    if request.method == "POST":
        data = Student.objects.get(pk=id)
        data.delete()
        return redirect('/teacher/show_student/')