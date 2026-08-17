from django import forms
from django.contrib.auth.models import User
class AccountForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={
            'password': forms.PasswordInput(),
            'email': forms.EmailInput()
        }