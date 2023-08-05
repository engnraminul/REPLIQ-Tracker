from django.db import models
from django.contrib.auth.models import User

#Company Models
class Company(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#Employee Models
class Employee(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    position = models.CharField(max_length=50, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

#Device Models
class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

#Device Log Models
class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    condition_on_checkout = models.CharField(max_length=100)
    condition_on_return = models.CharField(max_length=100, null=True, blank=True)