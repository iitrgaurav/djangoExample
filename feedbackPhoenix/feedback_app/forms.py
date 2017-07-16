from django import forms
from django.contrib.auth.models import User
from django.core import validators
from feedback_app.models import UserProfileInfo

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class  UserProfileInfoForm(forms.ModelForm):
    feedback = forms.CharField(widget=forms.Textarea)

    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic', 'feedback')
