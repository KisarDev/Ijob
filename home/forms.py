from django import forms
from . import models
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = '__all__'

   
class UserForm(forms.ModelForm):
    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario

    class Meta:
        model = User
        fields = ('username', 'password')
        
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    


# # creating a form
# class InputForm(forms.Form):
  
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length = 200)
#     roll_number = forms.IntegerField(
#                      help_text = "Enter 6 digit roll number"
#                      )
#     password = forms.CharField(widget = forms.PasswordInput())