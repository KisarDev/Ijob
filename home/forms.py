from django import forms
from . import models
from django.contrib.auth.models import User


   
class UserForm(forms.ModelForm):
        password = forms.CharField(
            label="password",
            strip=False,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
            help_text='Use the same password as before.',
            required=False,
        )
     
        password2 = forms.CharField(
            label="Confirmar_senha",
            strip=False,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
            help_text='Use the same password as before.',
            required=False,
        )
        class Meta:
            model = User
            fields = ['username', 'password',]

        def clean(self, *args, **kwargs):
              ...
        
