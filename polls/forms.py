from django import forms


class myUserForm(forms.Form):
    side_1 = forms.IntegerField()
    side_2 = forms.IntegerField()
