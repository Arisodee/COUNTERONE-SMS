from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Add_user


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['profile_pic', 'bio']


class Add_userForm(forms.ModelForm):
    class Meta:
        model = Add_user
        fields = ('full_name', 'id_number','phone_number', 'email')


class EditSupervisor(forms.ModelForm):
    class Meta:
        model = Add_user
        fields = ('full_name', 'id_number','phone_number', 'email')

