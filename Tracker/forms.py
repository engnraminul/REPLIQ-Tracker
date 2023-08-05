from django import forms
from .models import Company, Employee, Device

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
        fields = ['name', 'position', ]


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['model', 'category',]



class CheckoutForm(forms.Form):
    employee_name = forms.ChoiceField(choices=[])  # Initialize with empty choices
    checkout_condition = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company')
        super(CheckoutForm, self).__init__(*args, **kwargs)
        employee_choices = [(employee.name, employee.name) for employee in company.employee_set.all()]
        self.fields['employee_name'].choices = employee_choices