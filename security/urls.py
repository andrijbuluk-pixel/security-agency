from django.urls import path

from .views import (
    index,
    GuardListView,
    ClientListView,
    GuardCreateView,
    GuardDetailView,
    GuardLicenseUpdateView,
    GuardDeleteView,

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

    path("client/", ClientListView.as_view(), name="client-list"),

]

app_name = "security"
