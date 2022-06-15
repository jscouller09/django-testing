from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'your placeholder'}))
    
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if 'cfe' not in title:
            raise forms.ValidationError('This is not a valid title')
        return title