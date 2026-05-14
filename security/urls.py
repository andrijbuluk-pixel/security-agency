from django.urls import path

from .views import (
    index,
    GuardListView,
    ClientListView,
)

urlpatterns = [
    path('', index, name='index'),
    path("guard/", GuardListView.as_view(), name="guard-list"),
    path("client/", ClientListView.as_view(), name="client-list"),
]

app_name = "security"
