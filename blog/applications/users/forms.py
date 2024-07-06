#
from django import forms
#
from .models import User
#
from django.contrib.auth import authenticate


class CreateUserForm(forms.ModelForm):

    password1 = forms.CharField(
        required=True,
        label='Contraseña',
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña'
            }
        )
    )


    password2 = forms.CharField(
        required=True,
        label='Contraseña',
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirme Contraseña'
            }
        )
    )


    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'genero',
            'date_birth',
        )

        widgets = {
            'email' : forms.EmailInput(
                attrs={
                    'placeholder' : 'Ingrese su correo electronico'
                }
            ),

            'full_name' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese nombre completo'
                }
            ),

            'ocupation' : forms.TextInput(
                attrs={
                    'placeholder' : 'Tecnico, Tecnologo, Ingeniero ...'
                }
            ),

            'date_birth' : forms.DateInput(
                attrs={
                    'type' : 'date'
                }
            ),
        }
    

    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError('Las contraseñas no coinciden')
        
        return password2



class LoginForm(forms.Form):

    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder' : 'Email de usuario'
            }
        )
    )


    password = forms.CharField(
        required=True,
        label='Contraseña',
        widget= forms.PasswordInput(
            attrs=
            {
                'placeholder' : 'Contraseña de usuario'
            }
        )
    )


    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        email = self.cleaned_data['email']
        password = self.cleaned_data['password']        

        if not authenticate(email=email, password=password):
            return self.add_error('password', 'Usuario o contraseña erroneo')
        
        return self.cleaned_data