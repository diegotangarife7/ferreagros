from django import forms
from django.contrib.auth import authenticate

from .models import User



class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'type': 'password',
                'class': 'form-control'
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmar Contraseña',
                'type': 'password',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User

        fields = (
            'email',
            'name'
        )

        widgets = {

            'email': forms.EmailInput(
                attrs={
                        'placeholder': 'Correo',
                        'type': "email",
                        'class': 'form-control',
                    }
                ),

            'name': forms.TextInput(
                attrs={
                        'placeholder': 'Nombre',
                        'type': "text",
                        'class': 'form-control',
                    }
                ),
        }


    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')
        
        if len(self.cleaned_data['password1']) <= 5:
            self.add_error('password1', 'Utiliza una contraseña de 6 o mas caracteres')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está en uso.')
        return email



class LoginForm(forms.Form):
    email = forms.CharField(
        label = 'Correo',
        required = True,
        widget = forms.EmailInput(
            attrs={
                'placeholder': 'Correo...',
                'class': 'form-control',
            }
        )
    )

    password = forms.CharField(
        label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña...',
                'class': 'form-control',
            }
        )
    )

    def clean(self):
        super().clean()

        try:
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
        except:
            raise forms.ValidationError('Ha ocurrido un error. Intenta de nuevo.')
        
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos no son correctos')

        return self.cleaned_data
    
    def non_field_errors(self):
        errors = super().non_field_errors()
        if 'Los datos no son correctos' in errors:
            return errors
        return []



class UpdatePasswordForm(forms.Form):
    old_password = forms.CharField(required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Su contraseña actual',
                'class': 'form-control',
            }
        )
    )

    new_password_1 = forms.CharField(required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Nueva Contraseña',
                'class': 'form-control',
            }
        )
    )

    new_password_2 = forms.CharField(required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repita nueva contraseña',
                'class': 'form-control',
            }
        )
    )

    def clean(self):
        super().clean()

        try:
            old_password = self.cleaned_data['old_password']
            new_password_1 = self.cleaned_data['new_password_1']
            new_password_2 = self.cleaned_data['new_password_2']
        except:
            raise forms.ValidationError('Ha ocurrido un error. Intenta de nuevo.')

        if new_password_1 != new_password_2:
            raise forms.ValidationError('Las contraseñas no coinciden //')
        elif len(new_password_1) <= 5:
            raise forms.ValidationError('Utiliza una contraseña de 6 o mas caracteres.')
        elif new_password_1 == old_password:
            raise forms.ValidationError('Se ha producido un error. Asegúrate de introducir correctamente tu contraseña actual y de elegir una nueva contraseña diferente.')
        