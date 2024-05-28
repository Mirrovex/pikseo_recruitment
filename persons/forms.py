from django import forms

from .models import Persons


class NameForm(forms.Form):
    names = Persons.objects.values_list('first_name', flat=True).distinct().order_by('first_name')
    name_choices = [('', 'Wybierz imię')] + [(name, name) for name in names]

    first_name = forms.ChoiceField(
        choices=name_choices,
        label="",
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Full Name'
        })
    )
