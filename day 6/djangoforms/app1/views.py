from django.shortcuts import render
from app1.forms import InputForm,StudentForm
# Create your views here.
def input_form(request):
    if request.method =='POST':
        form=InputForm(request.POST)
        # if form.is_valid():
        #     form.save()
    else:
        form=InputForm()
    return render(request,'app1/input-form.html',{'form':form})

def student_form(request):
    form=StudentForm()
    return render(request,'app1/student-form.html',{'form':form})