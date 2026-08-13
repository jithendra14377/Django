from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def calculator(request):
    if request.method == 'POST':
        name = request.POST['name']
        a=int(request.POST['a'])
        b = int(request.POST['b'])
        op = request.POST['op']
        c=0
        if op == 'add':
            c = a + b
        elif op == 'sub':
            c = a- b
        elif op == 'div':
            c = a/ b
        elif op == 'mul':
            c = a * b
        context = {'name': name, 'a': a, 'b': b,'c':c,'op':op}
        return render(request,'myapp/calcresponse.html',context)
    return render(request,'myapp/calculator.html')