from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *



'''
class index(forms.Form):

    email = forms.EmailField()

    password = forms.CharField()
'''

class signup(UserCreationForm):

    email = forms.EmailField(required=True)

    first_name = forms.CharField(max_length=50, required=True)

    last_name = forms.CharField(max_length=50, required=True)



    class Meta:

        model = User


        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  ]

    def save(self, commit=True):
        USER = super(signup, self).save(commit=False)

        USER.first_name = self.cleaned_data['first_name']
        USER.last_name = self.cleaned_data['last_name']
        USER.email_name = self.cleaned_data['email']

        if commit:
            USER.save()
            
        return USER


class edit_info(UserChangeForm):

    class Meta:

        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'password']



class add_house_image(forms.Form):

   image = forms.FileField(required=True)
