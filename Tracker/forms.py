from django import forms
from .models import Company, Employee

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        instance.created_by = user
        if commit:
            instance.save()
        return instance
    
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name' ]