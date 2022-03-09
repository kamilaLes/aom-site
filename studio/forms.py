from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={'class':'form-control'}),
            "last_name": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.TextInput(attrs={'class':'form-control'}),
            "phone": forms.TextInput(attrs={'class':'form-control','placeholder':"(+48)"}),
            "classes": forms.CheckboxSelectMultiple(attrs={'class':'form-check-inline'})
        }

