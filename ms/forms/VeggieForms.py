from django import forms

class SearchForm(forms.Form):
    content = forms.CharField(label='Find..', max_length=256)
