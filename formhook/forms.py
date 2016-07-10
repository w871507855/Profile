from django import forms


class PersonalInfo(forms.Form):
    name = forms.CharField(max_length=50, label='Your name', strip=True)
    date_of_birth = forms.DateField(
        label='Date of birth',
        input_formats=['%Y-%m-%d'],
        help_text='format example: 2016-01-01'
    )
    email = forms.EmailField(label='Email address')
    introduction = forms.CharField(
        widget=forms.Textarea,
        label='Self introduction',
        required=False
    )






