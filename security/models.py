from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Client(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)

    username = models.CharField(
        max_length=255,
        unique=True,
        default="",
    )

    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default=""
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default=""
    )


class ProtectionType(models.Model):
    type = models.TextField()

    def __str__(self):
        return self.type


class Contract(models.Model):
    number_document = models.CharField(max_length=255)
    signing = models.DateField()
    validity_period = models.DurationField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.number_document


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    inventory_number = models.CharField(max_length=255)


class Guard(models.Model):
    username = models.CharField(max_length=255, default="")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    callsign = models.CharField(max_length=255)
    badge_number = models.CharField(max_length=255)
    contract_phone = models.CharField(max_length=255)
    equipment = models.ManyToManyField(Equipment)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("security:guard-detail", kwargs={"pk": self.pk})


class Object(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    type_protection = models.ForeignKey(ProtectionType, on_delete=models.CASCADE)
    guardian = models.ManyToManyField(Guard)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)


class Event(models.Model):
    timestamp = models.DateTimeField()
    description = models.TextField()
    guard = models.ForeignKey(Guard, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
