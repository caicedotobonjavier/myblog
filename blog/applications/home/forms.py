#
from django import forms
#
from .models import Suscribers, Contact

class SuscribersForm(forms.Form):

    email = forms.EmailField(
        label='Email',
        required=True,
        widget= forms.EmailInput(
            attrs={
                'placeholder' : 'Ingrese Correo Electronico'
            }
        )
    )



class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'full_name',
            'email',
            'messagge',
        )