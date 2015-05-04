from django import forms
from cowork.models import *


class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', )
        labels = {
            'name': 'Company name'
        }


class LocationCreationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('city', 'total_desks', 'reserved_desks', 'price')


class DeskCreationForm(forms.ModelForm):
    class Meta:
        model = Desk
        fields = ('rent_start_date', 'rent_end_date')
        labels = {
            'rent_start_date': 'Date of start rent',
            'rent_end_date': 'Date of end rent'
        }
