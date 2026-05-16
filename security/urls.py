from django.urls import path

from .views import (
    index,
    GuardListView,
    ClientListView,
    GuardCreateView,

)

urlpatterns = [
    path('', index, name='index'),
    path("guard/", GuardListView.as_view(), name="guard-list"),
    path("client/", ClientListView.as_view(), name="client-list"),

    path("guard/created/", GuardCreateView.as_view(), name="guard-created"),
]

app_name = "security"
