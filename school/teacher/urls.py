from django.urls import path
from .views import *

urlpatterns = [
    path('', teacher_home, name='teacher_home'),
    path('add_student/', add_student, name='add_student'),
    path('show_student/', show_student, name='show_student'),

    #Update data
    path('update/<int:id>/', update_data, name='update_data'),
    #Delete Data
    path('delete/<int:id>/', delete_data, name='delete_data'),
]