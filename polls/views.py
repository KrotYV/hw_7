from django.shortcuts import render

from .forms import myUserForm


def index(request):
    side_3 = 0
    message_err = ''
    if request.method == "POST":
        form = myUserForm(request.POST)
        if form.is_valid():
            side_1 = form.cleaned_data['side_1']
            side_2 = form.cleaned_data['side_2']

            if side_1 > 0 and side_2 > 0:
                side_3 = round((side_1 ** 2 + side_2 ** 2) ** 0.5)
            else:
                message_err = 'Значение сторон должно быть больше 0'

        UserForm = myUserForm()

    else:
        UserForm = myUserForm()

    return render(request, "index.html", {"side_3": side_3, "form": UserForm, "message_err": message_err})
