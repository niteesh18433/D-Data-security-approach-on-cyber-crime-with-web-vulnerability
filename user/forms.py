from django import forms

from user.models import RegisterModel


class RegisterForms(forms.ModelForm):
    class Meta:
        model=RegisterModel
        fields=("firstname","lastname","userid","password","email","gender","mblenum",)