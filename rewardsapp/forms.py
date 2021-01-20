
from django import forms
from .models import Employee, Employee_Reward, Reward

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('number', 'firstname', 'lastname', 'active')

class RewardForm(forms.ModelForm):

    class Meta:
        model = Reward
        fields = ('name','description')


class EmployeeRewardForm(forms.ModelForm):
    class Meta:
        model = Employee_Reward
        fields = ('employee', 'reward')