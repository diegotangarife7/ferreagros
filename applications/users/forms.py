from django import forms

from .models import User

from django.core.validators import validate_email

from django.contrib import messages




class UserRegisterForm(forms.ModelForm):

    password_1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'form-control'
                
            }
        )
    )

    password_2 = forms.CharField(
        label='Confirmaciíon de contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmacion de contraseña',
                'class': 'form-control'
            }
        )
    )


    class Meta:
        model = User
        fields = (
            'first_name',
            'genre',
            'email',
        )

        labels = {
            'first_name': 'Nombre',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                    'placeholder': 'Nombre',
                    'class': 'form-control',
                }
            ),

            'genre': forms.Select(attrs={
                    'class': 'form-select',
                }
            ),

            'email': forms.EmailInput(attrs={
                    'placeholder': 'Example@example.com',
                    'class': 'form-control'
                }
            )
        }

        # required = {
        #     'first_name':True,
        #     'genre': False
        # }
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya ha sido registrado. Por favor, use otro.')
        
    def clean_password_2(self):
        if self.cleaned_data['password_1'] != self.cleaned_data['password_2']:
            self.add_error('password_2', 'Las contraseñas no coinciden') 
        if len(self.cleaned_data['password_1']) <= 7:
            self.add_error('password_1', 'La contraseña debe ser de minimo 8 catacteres') 


