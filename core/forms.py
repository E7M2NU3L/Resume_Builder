from typing import Any
from django import forms
from .models import SigninWithRegister

class Register(forms.ModelForm):
    
    class Meta:
        Model = SigninWithRegister
        fields = ['email', 'first_name', 'last_name'  'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)