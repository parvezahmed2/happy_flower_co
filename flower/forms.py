from django import forms
from .models import  Flower

class PostForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = '__all__'
         