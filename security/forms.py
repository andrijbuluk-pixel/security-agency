from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from security.models import Guard, Object, Contract, Event, Client


class GuardForm(forms.ModelForm):
    guard = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Guard
        fields = "__all__"


class GuardCreationForm(forms.ModelForm):
    class Meta:
        model = Guard
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "callsign",
            "badge_number",
            "contract_phone",
            "equipment",
        )

        widgets = {
            "equipment": forms.CheckboxSelectMultiple,
        }

    def clean_license_number(self):
        return validate_license_number(
            self.cleaned_data
            ["badge_number"]
        )


class GuardLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Guard
        fields = [
            "contract_phone",
            "callsign",
            "badge_number",
            "equipment",
        ]

    widgets = {
        "equipment": forms.CheckboxSelectMultiple,
    }

    def clean_license_number(self):
        return validate_license_number(
            self.cleaned_data[
                "badge_number",
                "callsign",
                "contract_phone",
            ]
        )


class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "number_document",
            "signing",
            "validity_period",
            "price",
        ]

        widgets = {
            "signing": forms.DateInput(attrs={"type": "date"}),
            "validity_period": forms.NumberInput(
                attrs={"placeholder": "Number of days"}
            ),
        }


class ObjectCreateForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
    )

    class Meta:
        model = Object
        fields = [
            "name",
            "address",
            "type_protection",
            "client",
            "guardian",
            "contract",
        ]

        widgets = {
            "contract": forms.Select,
            "guardian": forms.SelectMultiple,
            "type_protection": forms.Select,
        }


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "timestamp",
            "description",
            "guard",
            "object"
        ]

        widgets = {
            "timestamp": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M"
            ),
        }


class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]

        widgets = {
            "username": forms.TextInput(),
            "last_name": forms.TextInput(),
            "first_name": forms.TextInput(),
            "email": forms.EmailInput(),
            "password1": forms.PasswordInput(),
            "password2": forms.PasswordInput(),
        }


def validate_license_number(
        license_number,
):
    if len(license_number) != 8:
        raise ValidationError("License number should consist of 8 characters")
    elif not license_number[:2].isupper() or not license_number[:2].isalpha():
        raise ValidationError("First 3 characters should be uppercase letters")
    elif not license_number[3:].isdigit():
        raise ValidationError("Last 5 characters should be digits")

    return license_number


class GuardUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your username",
            }
        )
    )


class ObjectNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your username",
            }
        )
    )


class ClientNameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your username",
            }
        )
    )
