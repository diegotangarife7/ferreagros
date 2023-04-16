from django import forms

from .models import AboutUs


class ContactForm(forms.Form):

    name = forms.CharField(
        required=True, 
        max_length=50,
        widget=forms.TextInput(
            attrs= {
                    'class': 'style-inputs-form'
                }
            )
        )
    
    email = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.EmailInput(
            attrs= {
                    'class': 'style-inputs-form'
                }
            )
        )
        
    phone = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs= {
                    'class': 'style-inputs-form'
                }
            )
        )
    
    subject = forms.CharField(
        required=True, 
        max_length=50,
        widget=forms.TextInput(
            attrs= {
                    'class': 'style-inputs-form'
                }
            )
        )

    message = forms.CharField(
        required=True, 
        widget=forms.Textarea(
            attrs= {
                    'class': 'style-inputs-form input-textarea-user'
                }
            )
        )
    
    notification = forms.BooleanField(
        initial=False,
        required=False,
        widget=forms.CheckboxInput(
            attrs= {
                    'class': ''
                }
            )
        )
    


class AboutUsForm(forms.ModelForm):
    
    class Meta:
        model = AboutUs
        fields = [
            'title',
            'description',
            'principal_image',
            'title_1',
            'description_title_1',
            'avatar',
            'name_avatar',
            'description_avatar',
            'title_2',
            'description_title_2',
            'title_3',
            'description_title_3',
        ]

    
    

    


       