from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib import messages

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    password = forms.CharField(
        label="password",
        strip=False,
        widget=forms.PasswordInput(),
        help_text='Use the same password as before.',
        required=True,
        error_messages={
            'required': 'Password must not be empty'
        }
    )

    password2 = forms.CharField(
        label="password2",
        strip=False,
        widget=forms.PasswordInput(),
        help_text='Use the same password as before.',
        required=True,
        error_messages={
            'required': 'Please, repeat your password'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data['username']
        password = cleaned_data['password']
        password2 = cleaned_data['password2']
        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
        
        if len(password) < 6:
            print(f"As senhas não podem ter menos de 6 caracteres e a sua tem {len(password)}")
            raise ValidationError("A senha deve ter pelo menos 6 caracteres", code='password_too_short')
        
        
        if username == password:
            print("O nome de usuário e a senha não podem ser iguais!!")
            raise ValidationError({"username":"O nome de usuário e a senha não podem ser iguais!!"})
            

        

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Use set_password para garantir o hashing correto
        if commit:
            user.save()
        return user
