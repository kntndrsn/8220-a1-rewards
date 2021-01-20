from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from django.utils import timezone

import datetime

from rewardsapp.models import Employee, Reward, Employee_Reward

from rewardsapp.forms import EmployeeForm, RewardForm, EmployeeRewardForm

from django.shortcuts import render, get_object_or_404, redirect

from django.conf import settings

@login_required
def employee_list(request):

    employees = Employee.objects.all()

    return render(request, 'employee_list.html', {'employees': employees})

@login_required
def employee_new(request):

    if request.method == "POST":

        form = EmployeeForm(request.POST)

        if form.is_valid():

            employee = form.save(commit=False)

            employee.created_by = request.user
            employee.save()

            return redirect('rewardsapp:employee_list')
    else:
        return render(request, 'employee_form.html', {'form': EmployeeForm()})

@login_required
def employee_edit(request, employee_id):

   employee = get_object_or_404(Employee, pk=employee_id)

   if request.method == "POST":
       
       form = EmployeeForm(request.POST, instance=employee)

       if form.is_valid():

           employee = form.save(commit=False)

           employee.updated = timezone.now()

           employee.save()
           
           return redirect('rewardsapp:employee_list')
        
   else:
    
       form = EmployeeForm(instance=employee)

       return render(request, 'employee_form.html', {'form': form, 'employee': employee})

@login_required
def employee_delete(request, employee_id):

    employees = get_object_or_404(Employee, pk=employee_id)

    employees.delete()

    return redirect('rewardsapp:employee_list')



@login_required
def reward_list(request):

    rewards = Reward.objects.all()

    return render(request, 'reward_list.html', {'rewards': rewards})

@login_required
def reward_new(request):

    if request.method == "POST":

        form = RewardForm(request.POST)

        if form.is_valid():

            reward = form.save(commit=False)

            reward.save()

            return redirect('rewardsapp:reward_list')
    else:
        return render(request, 'reward_form.html', {'form': RewardForm()})

@login_required
def reward_edit(request, reward_id):

   reward = get_object_or_404(Reward, pk=reward_id)

   if request.method == "POST":
       
       form = RewardForm(request.POST, instance=reward)

       if form.is_valid():

           reward = form.save(commit=False)

           reward_id.save()
           
           return redirect('rewardsapp:reward_list')
        
   else:
    
       form = RewardForm(instance=reward)

       return render(request, 'reward_form.html', {'form': form})

@login_required
def reward_delete(request, reward_id):

    reward = get_object_or_404(Reward, pk=reward_id)

    reward.delete()

    return redirect('rewardsapp:reward_list')


# Employee Reward
@login_required
def employee_reward_list(request, employee_id):

    employee = get_object_or_404(Employee, pk=employee_id)

    employee_rewards = Employee_Reward.objects.filter(employee_id=employee_id)

    return render(request, 'employee_reward_list.html', {'employee_rewards': employee_rewards, 'employee': employee})

@login_required
def employee_reward_delete(request,  employee_reward_id, employee_id):

    employeeReward = get_object_or_404(Employee_Reward, pk=employee_reward_id)

    employeeReward.delete()

    return redirect('rewardsapp:employee_reward_list', employee_id=employee_id)

@login_required
def employee_reward_new(request, employee_id):

    if request.method == "POST":

        form = EmployeeRewardForm(request.POST)

        if form.is_valid():

            employeeRewardForm = form.save(commit=False)

            employeeRewardForm.awarded_on = timezone.now()

            employeeRewardForm.awarded_by = request.user

            employeeRewardForm.save()

            return redirect('rewardsapp:employee_reward_list', employee_id=employee_id)

    else:

        employee = Employee.objects.get(pk=employee_id)

        rewards = Reward.objects.all()

        form = EmployeeRewardForm(initial={"employee":employee, "rewards":rewards})

        return render(request, 'employee_rewards_form.html', {'form': form})