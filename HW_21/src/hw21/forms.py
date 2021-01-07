from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    age = forms.IntegerField(min_value=3, max_value=99)
    profession = forms.CharField(max_length=80)
