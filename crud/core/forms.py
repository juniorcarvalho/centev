from django import forms

from crud.core.models import People


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

