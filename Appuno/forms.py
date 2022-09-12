from django import forms
from .models import libros
from django.db.models import fields

class Formulariolibro(forms.ModelForm):

    class Meta:
        model = libros
        fields = '__all__'

        Widget={
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }