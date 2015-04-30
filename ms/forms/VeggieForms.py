from django import forms

CharField_attrs={'class':'form-control',
                 'placeholder':'Art Name, Artist, Museum...'
}

Submit_attrs={}

REGION_CHOICES = ((1,"Asian"),(2,"African"),(3,"North American"),(4,"Central & South American"),
(5,"Oceanian"),(7,"European"),(8,""))

STYLE_CHOICES = ((1,"realist"),(2,"abstract"),(3,"expressionist"),(4,"conceptual"),(5,""))

TYPE_CHOICES = ((1,"applied & decorative arts"),(2,"drawing"),(3,"painting"),(4,"photograph"),(5,"print"),
(6,"sculpture"),(7,"watercolor"),(8,""))


class SearchForm(forms.Form):
    content = forms.CharField(max_length=256, widget=forms.TextInput(CharField_attrs))

class SelectRegionForm(forms.Form):
    region_choice = forms.ChoiceField(label = "region_select",choices=REGION_CHOICES)

class SelectTypeForm(forms.Form):
    type_choice = forms.ChoiceField(label = "type_select",choices=TYPE_CHOICES)

class SelectStyleForm(forms.Form):
    style_choice = forms.ChoiceField(label = "style_select",choices=STYLE_CHOICES)
