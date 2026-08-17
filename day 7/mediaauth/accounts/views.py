from django.shortcuts import render,redirect
from .forms import AccountForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def account_register(request):
    if request.method == 'POST':
        form=AccountForm(request.POST)
        if form.is_valid():
            account=form.save(commit=False) 
            # commit=false ante first userdata direct daatabase lo store avvakunda danni object lo create ayyi 
            # danni reference anedi account variable ki pampistadi because it's use for temporarily storage
            account.set_password(form.cleaned_data['password'])
            account.save()
            return redirect(account_login)
    else:
        form=AccountForm()
    return render(request,'accounts/signupform.html',{'form':form})


def account_login(request):
    if request.user.is_authenticated:
        return redirect(account_dashboard)
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user != None:
            login(request,user)
            return redirect(account_dashboard)
        else:
            return HttpResponse('Invalid Response')
    return render(request,'accounts/loginform.html')

def account_logout(request):
    logout(request)
    return redirect(account_login)
def account_home(request):
    return render(request,'accounts/home.html')

@login_required
def account_dashboard(request):
    return  render(request,'accounts/dashboard.html')