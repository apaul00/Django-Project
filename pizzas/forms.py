from django import forms

from .models import Pizza, Comment, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['pizza_name']
        labels = {'pizza_name': ''}

