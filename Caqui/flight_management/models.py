from unittest.util import _MAX_LENGTH
from django.db import models
from flight_management.enums import AirportCodes, Status, Role
from datetime import datetime

# tx = text
# dt = datetime
# nm = enums 
# fk = foreign key

# TODO: verificar passagem de timezone

class FlightStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    dt_departure = models.DateTimeField(blank=True, null=True)
    dt_arrival = models.DateTimeField(blank=True, null=True)
    nm_status = models.IntegerField(choices=Status.choices, default=0)
    dt_creation = models.DateTimeField(auto_now=True)
    dt_updated = models.DateTimeField(auto_now=True)
    dt_done = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'flight_status'

class Flight(models.Model):
    id = models.BigAutoField(primary_key=True)
    fk_flightstatus = models.ForeignKey(FlightStatus, on_delete=models.SET_NULL, blank=True, null=True)
    tx_code = models.CharField(max_length=8)
    dt_est_departure = models.DateTimeField()
    dt_est_arrival = models.DateTimeField()
    nm_origin = models.IntegerField(choices=AirportCodes.choices)
    nm_destination = models.IntegerField(choices=AirportCodes.choices)
    class Meta:
        db_table = 'flight'

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    tx_name = models.CharField(max_length=42)
    nm_role = models.IntegerField(choices=Role.choices, default=0)
    tx_username = models.CharField(max_length=42)
    tx_hash_key = models.CharField(max_length=64)
    class Meta:
        db_table = 'user'

