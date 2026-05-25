from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import (
    GuardUsernameSearchForm,
    GuardCreationForm,
    GuardLicenseUpdateForm,
    ObjectNameSearchForm,
    ContractCreateForm,
    ObjectCreateForm,
    EventCreateForm,
    ClientCreateForm,
)
from .models import Guard, Client, Object, Contract, Event


@login_required
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

        username = self.request.GET.get("username", "")

        context["search_form"] = GuardUsernameSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Guard.objects.prefetch_related("equipment")
        username = self.request.GET.get("username", "")

        if username:
            return queryset.filter(username__icontains=username)
        return queryset


class GuardCreateView(LoginRequiredMixin, generic.CreateView):
    model = Guard
    form_class = GuardCreationForm


class GuardDetailView(LoginRequiredMixin, generic.DetailView):
    model = Guard
    queryset = Guard.objects.all().prefetch_related("equipment")


class GuardLicenseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Guard
    form_class = GuardLicenseUpdateForm
    success_url = reverse_lazy("security:guard-list")


class GuardDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Guard
    success_url = reverse_lazy("security:guard-list")


class EventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    paginate_by = 10


class EventCreate(LoginRequiredMixin, generic.CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = "security/event_form.html"
    success_url = reverse_lazy("security:event-list")


class ObjectListView(LoginRequiredMixin, generic.ListView):
    model = Object
    context_object_name = "objects_list"
    template_name = "security/object_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ObjectListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = ObjectNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Object.objects.all()
        name = self.request.GET.get("name", "")

        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class ContractCreate(LoginRequiredMixin, generic.CreateView):
    model = Contract
    form_class = ContractCreateForm
    template_name = "security/object_form.html"
    success_url = reverse_lazy("security:new-object-list")


class ObjectCreate(LoginRequiredMixin, generic.CreateView):
    model = Object
    form_class = ObjectCreateForm
    template_name = "security/object_form.html"
    success_url = reverse_lazy("security:object-list")


class ObjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Object
    fields = "__all__"
    success_url = reverse_lazy("security:object-list")


class ObjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Object
    success_url = reverse_lazy("security:object-list")


class ObjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Object


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client
    form_class = ClientCreateForm
    success_url = reverse_lazy("security:client-detail")


class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client
    paginate_by = 5


class ClientCreate(LoginRequiredMixin, generic.CreateView):
    model = Client
    form_class = ClientCreateForm
    template_name = "security/client_form.html"
    success_url = reverse_lazy("security:client-list")


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Client
    success_url = reverse_lazy("security:client-list")
