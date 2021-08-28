from django import forms


class UserForm(forms.Form):
    side_1 = forms.IntegerField()
    side_2 = forms.IntegerField()
