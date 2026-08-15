from django.urls import path
from .views import student_create,student_delete,studenthome
urlpatterns=[
    path('student-home/',studenthome,name='student_home'),
    path('create/',student_create,name='student_create'),   
    path('<int:id>/delete', student_delete,name='student_delete')
]