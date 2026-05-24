from django.urls import path

from .views import (
    index,
    GuardListView,
    EventListView,
    GuardCreateView,
    GuardDetailView,
    GuardLicenseUpdateView,
    GuardDeleteView,
    ObjectListView,
    ContractCreate,
    ObjectCreate,
    ObjectDetailView,
    ClientListView,
    ObjectUpdateView,
    ObjectDeleteView,

)

urlpatterns = [
    path('', index, name='index'),
    path("guard/", GuardListView.as_view(), name="guard-list"),
    path("guard/created/", GuardCreateView.as_view(), name="guard-created"),
    path(
        "guard/<int:pk>/", GuardDetailView.as_view(), name="guard-detail"
    ),
    path(
        "guard/<int:pk>/update/",
        GuardLicenseUpdateView.as_view(),
        name="guard-update",
    ),
    path(
        "guard/<int:pk>/delete/",
        GuardDeleteView.as_view(),
        name="guard-delete",
    ),

    path("event/", EventListView.as_view(), name="event-list"),

    path("object/", ObjectListView.as_view(), name="object-list"),
    path("object/contract/", ContractCreate.as_view(), name="contract-list"),
    path("object/contract/new-object", ObjectCreate.as_view(), name="new-object-list"),
    path("object/<int:pk>/", ObjectDetailView.as_view(), name="object-detail-list"),
    path("object/<int:pk>/update", ObjectUpdateView.as_view(), name="object-update-list"),
    path("object/<int:pk>/delete", ObjectDeleteView.as_view(), name="object-delete-list"),

    path("client/<int:pk>/", ClientListView.as_view(), name="client-detail"),
]

app_name = "security"
