from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title of the article'}))
    author = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Author of the article'}))
    
    class Meta:
        model = Article
        fields = [
            'title',
            'author',
            'content',
            'active',
        ]
