from django import forms
from functools import partial
from .models import Project

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

PROJECT_CHOICES = [tuple([x, x]) for x in Project.objects.all()]


class LogTime(forms.Form):
    duration = forms.FloatField(
        label='DURATION ', required=False, min_value=0, max_value=24)

    project = forms.CharField(label='PROJECT ', max_length=64,
                              required=False, widget=forms.Select(choices=PROJECT_CHOICES))

    remarks = forms.CharField(label='REMARKS ', max_length=200, required=False)

    date = forms.DateField(label='Select date ', widget=DateInput())
