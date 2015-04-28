from django import forms

CharField_attrs={'class':'form-control',
                 'placeholder':'Art Name, Artist, Museum...'
}

Submit_attrs={}

class SearchForm(forms.Form):
    content = forms.CharField(max_length=256, widget=forms.TextInput(CharField_attrs))
