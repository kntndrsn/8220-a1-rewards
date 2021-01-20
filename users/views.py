from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from users.forms import UserForm, UserFormUpdate

@login_required
@user_passes_test(lambda user: user.is_superuser)
def user_list(request):

    users = User.objects.all().order_by('-date_joined')

    return render(request, 'user_list.html', {'users': users})


@login_required
@user_passes_test(lambda user: user.is_superuser)
def user_edit(request,pk):
    user = get_object_or_404(User,pk=pk)

    if request.method == "POST":
        
        form = UserFormUpdate(request.POST, instance= user)

        if form.is_valid():

            user = form.save(commit=False)

            user.save()

            return redirect('user_list')

    else:
        form = UserFormUpdate(instance= user)

        return render(request, 'user_form.html', {'form': form})

@login_required
@user_passes_test(lambda user: user.is_superuser)
def user_new(request):

    if request.method == "POST":

        form = UserForm(request.POST)
        
        if form.is_valid():

            user = None

            if form.cleaned_data['is_superuser'] == True:

                user = User.objects.create_superuser(username=form.cleaned_data['username'],
                                                     email=form.cleaned_data['email'],
                                                     password=form.cleaned_data['password'],
                                                     first_name=form.cleaned_data['first_name'],
                                                     last_name=form.cleaned_data['last_name'],)
            else:
                user = User.objects.create_user(username=form.cleaned_data['username'],
                                                email=form.cleaned_data['email'],
                                                password=form.cleaned_data['password'],
                                                first_name=form.cleaned_data['first_name'],
                                                last_name=form.cleaned_data['last_name'],)

            user.save()

            return redirect('user_list')

    else:
        return render(request, 'user_form.html', {'form': UserForm()})

@login_required
@user_passes_test(lambda user: user.is_superuser)
def user_delete(request, pk):

    user = get_object_or_404(User, pk=pk)

    user.delete()

    return redirect('user_list')