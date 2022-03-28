from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import fields

from .models import Question,  Profile

# class ProfileImageForm(forms.ModelForm):
#     class Meta: 
#         model = ProfileImage
#         fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserQuestions(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
        labels = {
            "question": "Ask the question ?"
        }

class UserUpdateForm(forms.ModelForm):
     class Meta:
         model = User
         fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']




        

