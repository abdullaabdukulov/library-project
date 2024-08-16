from django import forms
from .models import Author, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'published_at', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'published_at': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'created_by': forms.HiddenInput(),
        }

    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
