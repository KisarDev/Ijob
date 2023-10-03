from django import forms
from .models import Usuario
from django.contrib.auth.models import User

# class UserFormChoices(forms.ModelForm):
    
#     class Meta:
#         model = Usuario
#         fields = ('modalidade',)


   
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
            fields = ['username', 'password','password2']

        def clean(self, *args, **kwargs):
              ...
        
