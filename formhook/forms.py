from django import forms
from .models import PersonalInfor


class PersonalInforForm(forms.ModelForm):
    class Meta:
        model = PersonalInfor
        # fields = ['name', 'date_of_birth', 'email', 'introduction']
        fields = '__all__'
        widgets = {
            'introduction': forms.Textarea(attrs={'cols': 25, 'rows': 5}),
            'name': forms.TextInput(attrs={'title':'Your name', 'required': True}),
            'email': forms.TextInput(attrs={'required': True}),
        }


class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    url = forms.URLField()
    comment = forms.CharField(
        widget=forms.TextInput(attrs={'size': '40', 'title': 'Fill in your name'})
    )



















