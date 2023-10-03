from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

class UserForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=True,
    )

    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=True,
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.data.get('password2')
        if password != password2:
            print(password, password2)
            raise forms.ValidationError("As senhas não coincidem.")
        return password

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Use set_password para garantir o hashing correto
        if commit:
            user.save()
        return user
