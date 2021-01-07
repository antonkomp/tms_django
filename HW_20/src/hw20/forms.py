from django import forms


class TicketForm(forms.Form):
    name = forms.CharField(max_length=50)
    from_where = forms.CharField(max_length=50)
    where_to = forms.CharField(max_length=50)
    amount_of_peoples = forms.IntegerField(min_value=1, max_value=10)
    date = forms.DateField(widget=forms.SelectDateWidget())
