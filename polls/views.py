from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm


def index(request):
    if request.method == "POST":
        side_1 = int(request.POST.get("side_1"))
        side_2 = int(request.POST.get("side_2"))
        if side_1 > 0 and side_2 > 0:
            side_3 = round((side_1 ** 2 + side_2 ** 2) ** 0.5)
            return HttpResponse(f"<h2>Если катеты треугольника {side_1} и {side_2}, то гипотенуза {side_3}</h2>")
        else:
            userform = UserForm()
            return render(request, "index.html", {"form": userform})
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})
