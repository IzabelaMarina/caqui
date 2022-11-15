from django.db import models
from flight_management.enums import AirportCodes, Status, Role
from datetime import datetime
from django.urls import reverse  # To generate URLS by reversing URL patterns

# tx = text
# dt = datetime
# nm = enums 
# fk = foreign key

# verificar passagem de timezone

class FlightStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    dt_departure = models.DateTimeField(blank=True, null=True)
    dt_arrival = models.DateTimeField(blank=True, null=True)
    nm_status = models.CharField(max_length=13, choices=Status.choices, default=Status.PREVISTO)
    dt_creation = models.DateTimeField(auto_now=True)
    dt_updated = models.DateTimeField(auto_now=True)
    dt_done = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'flight_status'

class Flight(models.Model):
    id = models.BigAutoField(primary_key=True)
    fk_flightstatus = models.ForeignKey(FlightStatus, on_delete=models.SET_NULL, blank=True, null=True)
    tx_code = models.CharField(max_length=8)
    dt_est_departure = models.DateTimeField(blank=True, null=True)
    dt_est_arrival = models.DateTimeField(blank=True, null=True)
    nm_origin = models.CharField(max_length=3, choices=AirportCodes.choices)
    nm_destination = models.CharField(max_length=3, choices=AirportCodes.choices)
    class Meta:
        db_table = 'flight'

    def get_absolute_url(self):
        """Returns the url to access a particular user instance."""
        return reverse('flight-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.id, self.tx_code)

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    tx_name = models.CharField(max_length=42)
    nm_role = models.CharField(max_length=24, choices=Role.choices)
    tx_username = models.CharField(max_length=42)
    tx_hash_key = models.CharField(max_length=64)
    class Meta:
        db_table = 'user'

    def get_absolute_url(self):
        """Returns the url to access a particular user instance."""
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.id, self.tx_username)

