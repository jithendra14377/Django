from django import forms
from django.core.exceptions import ValidationError
from app1.models import Student
class InputForm(forms.Form):
    username = forms.CharField(required=True,max_length=50)
    email = forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    age= forms.IntegerField()
    married= forms.BooleanField()

    def clean_age(self):
        age=self.cleaned_data.get('age')
        if age < 18 or age > 36:
            raise ValidationError('Age must be between 18 and 36')
        return age

    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        password=cleaned_data.get('password')
        if username == password:
            raise ValidationError("Username and Paswword cannot be same")
        return cleaned_data

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','age','rollno']

# syntax
'''
field validation:
def clean_filename():
   get field from cleaned data
   validation_logic
   return field

entire form validation
def clean():
  get cleaned_data
  validation logic
  return cleaned_data
'''