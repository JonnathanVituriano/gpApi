from django import forms
from .models import LivroModel

class LivroForm(forms.ModelForm):
    class Meta:
        model = LivroModel
        fields = ['titulo']