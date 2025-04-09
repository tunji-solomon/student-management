from django import forms
from . models import *
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):


   class Meta:
      
      model = Our_student
      fields = '__all__'
      widgets = {
         

         'student_number': forms.NumberInput(attrs={
            'class': 'form-control',
            'style':'width:300px',
            'placeholder':'Enter student number'
         }),

         'first_name': forms.TextInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter first name'
         }),

         
         'last_name': forms.TextInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter first name'
         }),
         'date_of_birth': forms.DateInput(attrs={
            'type': 'date',
            'min': '1900-01-01',
            'max': '2025-12-31',
            'class': 'form-control',  # for Bootstrap styling if used
         })

      }

      department = forms.ModelChoiceField(queryset=Our_student.objects.all())

      parent = forms.ModelChoiceField(queryset=Our_student.objects.all())
     

class UserForm(forms.ModelForm):
   class Meta:
      
      model = Our_user
      fields = ['first_name','last_name','username','email','phone','password','confirm_password']
      widgets = {
         

         'first_name': forms.TextInput(attrs={
            'class': 'form-control',
            'style':'width:300px',
            'placeholder':'Enter first name'
         }),

         'last_name': forms.TextInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter last name'
         }),

         
         'username': forms.TextInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter username'
         }),

         'email': forms.EmailInput(attrs={

            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter email'

         }),
         
          'phone': forms.NumberInput(attrs={
             'class':'form-control',
             'style':'max-width:300px',
             'placeholder':'Enter phone number'
          }),

          'password': forms.PasswordInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Enter password'
         }),

           'confirm_password': forms.PasswordInput(attrs={
            'class':'form-control',
            'style':'max-width: 300px',
            'placeholder':'Confirm password'
         })
      }

class LoginForm(forms.ModelForm):

   class Meta:

      model = Our_user
      fields = ['username','password']
      widgets = {

         'username': forms.TextInput(attrs={

            'class':'form-control',
            'style':'max-width:300px',
            'placeholder':'Enter username'

         }),

         'password': forms.PasswordInput(attrs={

            'class':'form-control',
            'style':'max-width:300px',
            'placeholder':'Enter password'
         })
      }