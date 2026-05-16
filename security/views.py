from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import GuardUsernameSearchForm, GuardCreationForm
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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GuardListView, self).get_context_data(**kwargs)

        context["search_form"] = GuardUsernameSearchForm()
        return context

    def get_queryset(self):
        queryset = Guard.objects.prefetch_related("equipment")
        username = self.request.GET.get("username", "")

        if username:
            return queryset.filter(username__icontains=username)
        return queryset


class GuardCreateView(generic.CreateView):
    model = Guard
    form_class = GuardCreationForm




class ClientListView(generic.ListView):
    model = Client
