from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'is_superuser']

        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        
        self.fields['is_superuser'].label = 'System Administrator'
        self.fields['is_superuser'].help_text = 'Administrators are able to add users.'

class UserFormUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser', )

    def __init__(self, *args, **kwargs):
        super(UserFormUpdate, self).__init__(*args, **kwargs)
        
        self.fields['is_superuser'].label = 'System Administrator'
        self.fields['is_superuser'].help_text = 'Administrators are able to add users.'