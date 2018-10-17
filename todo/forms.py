from django import forms
import datetime


class Task_Form(forms.Form):
    Title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    Description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':
        'Enter Description'}))
    Due_date = forms.DateField( widget=forms.DateInput(attrs={'class': 'form-control','placeholder': 'YY-MM-DD Format'}))
