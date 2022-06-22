from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core import validators
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *

def checkalpha(value):
    # if value.startswith("," | "!" | "." | "/" | "<" | ">" | "{"):
        # raise forms.ValidationError("This is invalid")
    if value.isalpha() == False:
        raise forms.ValidationError('This is Invalid.')

def checkuserame(value):
    if value.isalnum() == False:
        raise forms.ValidationError('Username should be alpha or digit only.!')
    # if value[1].isdigit() == True:
    #     raise forms.ValidationError("Username can't start start with dight!")


def checkemail(value):
    if User.objects.filter(email = value).exists():
        raise forms.ValidationError("This email is already taken try another")
# def validusername(value):
#     if User.objects.filter(username = value).exists:
#         raise forms.ValidationError("Username is inorrect")

class LoginForm(AuthenticationForm):
    username = forms.CharField(label = "Enter username:",
    error_messages={'request':"This field is required🤯"},
    widget=forms.TextInput(attrs={'class':'input'}))

    password = forms.CharField(label = "Enter Password:",
    error_messages={'request':"This field is required"},
     widget=forms.PasswordInput(attrs={'class':'input'}))
    fields = '__all__'
    labels = {'username':"Enter Username", 
    'password':'Enter Password'}
    
        

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label = 'Enter Password:',
     widget = forms.PasswordInput(attrs={'class':'input'}),
     error_messages= {'required':'This Password is required'})
    password2 = forms.CharField(label = 'Password Again', widget = forms.PasswordInput(attrs={'class':'input'}),
     error_messages= {'required':'This Password  is required'})
    first_name = forms.CharField(validators=[checkalpha],
    widget = forms.TextInput(attrs={'class':'input'}),
     error_messages= {'required':'First Name is required'})
    last_name = forms.CharField(validators=[checkalpha],
    widget = forms.TextInput(attrs={'class':'input'}),
    error_messages= {'required':'Last Name is required'})
    email = forms.CharField(validators=[checkemail],
    widget = forms.EmailInput(attrs={'class':'input'}),
    error_messages= {'required':'This Email is required'})
    username = forms.CharField(validators=[checkuserame],max_length=50,min_length=4,
    widget= forms.TextInput(attrs={'class':'input'}),
    error_messages={'required':'Username is required '})
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        labels = {
                'username':"Enter Username",
                ' first_name':"Enter F-Name",
                    'last_name':"Enter L-Name" ,
                    'email':"Enter Email"}
                    
        widgets = {'username':forms.TextInput(attrs= {'class':'myclass'}),
                    'first_name':forms.TextInput(attrs= {'class':'myclass'}),
                    'last_name':forms.TextInput(attrs= {'class':'myclass'}),
                    'email':forms.EmailInput(attrs= {'class':'myclass'})}


        # error_messages = {'username':{'required':'This username is Required'},
        #                 'first_name':{'required':'This field is Required'},
        #                 'last_name':{'required':'This field is Required'},
        #                 'email':{'required':'This field is Required'}}

 

class ChangePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label= " Enter New Password :",
      widget= (forms.PasswordInput(attrs= {'class':'input'})),
      error_messages={'required':'This is required'})
    new_password2 = forms.CharField(label= " Enter New Again :",
     widget= (forms.PasswordInput(attrs= {'class':'input'})),
     error_messages={'required':'This is required'})
    fields = '__all__'


# class ProfileForm(forms.Form):
#     # pp = forms.CharField(label= "Upload Your Profile", widget=(forms.ImageField))
#     class Meta:
#         model = Profile
#         fields = ('pp')
