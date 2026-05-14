from django.shortcuts import render
from django.views import generic

from .models import Guard, Client


def index(request):
    num_guard = Guard.objects.count()
    num_client = Client.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_guard": num_guard,
        "num_client": num_client,
        "num_visits": num_visits + 1,
    }

    return render(request, "security/index.html", context=context)


class GuardListView(generic.ListView):
    model = Guard



class ClientListView(generic.ListView):
    model = Client
