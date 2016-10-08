from django import forms
from . import models


class BookListForm(forms.ModelForm):

    class Meta:
        model   = models.BookList
        fields  = ['title', 'author', 'publisher', 'review', 'cover']
        widgets = {
            'title': forms.TextInput(attrs={
                    'placeholder': 'book title',
                    'class'      : 'form-control',
                }),
            'author': forms.TextInput(attrs={
                    'placeholder': 'author name',
                    'class'      : 'form-control',
                }),
            'publisher': forms.TextInput(attrs={
                    'placeholder': 'book title',
                    'class'      : 'form-control',
                }),
            'review': forms.Textarea(attrs={
                    'class'      : 'form-control',
                    'placeholder': 'Comments ...',
                    'rows'       : 3,
                    'cols'       : 20,
                }),
            'cover': forms.FileInput(attrs={
                    'class': 'btn',
                }),
        }
