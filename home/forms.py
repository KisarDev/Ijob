from django import forms
from . import models
from django.contrib.auth.models import User
'''
class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = '__all__'
        exclude = 'username'

   
class UserForm(forms.ModelForm):
    password1 = forms.CharField(required=False, widget=forms.PasswordInput(), label='senha'),
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(), label='confirmar_senha'),

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario

    class Meta:
        model = User

'''