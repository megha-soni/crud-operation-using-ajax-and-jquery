from django import forms
from .models import User


# made an form an applied widgets for adding bootstrap functionality
class RegisterForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['name','email','password']
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
        'email':forms.TextInput(attrs={'class':'form-control', 'id':'emailid'}),
        'password':forms.PasswordInput(attrs={'class':'form-control', 'id':'passwordid'})
        }