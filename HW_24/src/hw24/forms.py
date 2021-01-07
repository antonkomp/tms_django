from django import forms


class PictureForm(forms.Form):
    width = forms.IntegerField(required=True)
    height = forms.IntegerField(required=True)


class SendForm(forms.Form):
    from_whom = forms.EmailField(required=True)
    to_whom = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    picture = forms.URLField()
    message = forms.CharField(widget=forms.Textarea)
