from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 w-full'}),
            'last_name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 w-full'}),
            'email': forms.EmailInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 w-full'}),
        }