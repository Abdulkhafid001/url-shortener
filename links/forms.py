from django import forms
from .models import URL


class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = '__all__'
        fields = ['long_url','short_code','expiry','custom_alias', 'clicks']
        widgets = {
            'long_url': forms.Textarea(attrs={'rows':5})
        }