from django.db import models


class Client(models.Model):
    pseudonym = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

class ProtectionType(models.Model):
    type = models.TextField()


class Contract(models.Model):
    number_document = models.CharField(max_length=255)
    signing = models.DateField()
    validity_period = models.DurationField()
    price = models.DecimalField(decimal_places=2, max_digits=10)


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    inventory_number = models.CharField(max_length=255)


class Guard(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    callsign = models.CharField(max_length=255)
    badge_number = models.CharField(max_length=255)
    contract_phone = models.CharField(max_length=255)
    equipment = models.ManyToManyField(Equipment)


class Object(models.Model):
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
