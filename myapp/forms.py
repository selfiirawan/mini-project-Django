from django import forms
from myapp.models import Studio

class StudioForm(forms.ModelForm):
    class Meta:
        model = Studio
        fields = ["name", "city", "specialty", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "specialty": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }