from django import forms

from .models import User





class UserRegisterForm(forms.ModelForm):

    password_1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña'
            }
        )
    )

    password_2 = forms.CharField(
        label='Confirmaciíon de contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'confirmacion de contraseña'
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


    def clean_password_2(self):
        if self.cleaned_data['password_1'] != self.cleaned_data['password_2']:
            self.add_error('password_2', 'las contraseñas no coinciden') 
        if len(self.cleaned_data['password_1']) <= 5:
            self.add_error('password_1', 'la contraseña debe ser mas larga') 


