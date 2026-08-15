from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
# Create your views here.
def studenthome(request):
    students=Student.objects.all()
    return render(request,'students/studenthome.html',{'students':students})

def student_create(request):
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(studenthome)
    else:
        form=StudentForm()
    return render(request,'students/student_form.html' ,{'form':form})


def student_delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect(studenthome)