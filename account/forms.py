from pyexpat import model
from statistics import mode
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "username"
            }
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "********"
            }
        )
    )


class SignUPForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"username"
            }
        )
    )
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"First Name"
            }
        )
    )
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Last Name"
            }
        )
    )
    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password"
            }
        )
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Re-Password"
            }
        )
    )
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Example@gmail.com"
            }
        )
    )
    bio = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Add Bio"
            }
        )
    )
    phone = forms.IntegerField(
        widget= forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder":"+123456789"
            }
        )
    )
     

    class Meta:
        model = User
        fields = ('username','phone','bio','email','password1','first_name','last_name','password2','is_admin','is_buyer','is_seller')

    

class EditUserProfileForm(UserChangeForm):

    class Meta:
            model = User
            fields = ['first_name','last_name','phone','bio','profile_img']




