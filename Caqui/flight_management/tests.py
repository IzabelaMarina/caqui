from django.test import TestCase
from datetime import datetime
from flight_management.models import Flight, FlightStatus, User
from flight_management.enums import AirportCodes, Status, Role  

class FlightCRUDTest(TestCase):
    def setUp(self):
        Flight.objects.create(tx_code="GOL0000", dt_est_departure=datetime.now(), dt_est_arrival=datetime.now(), nm_origin="BSB", nm_destination="CGH", fk_flightstatus=FlightStatus.objects.create())

    def testCreated(self):
        voo = Flight.objects.get(tx_code="GOL0000")
        self.assertEqual(voo.tx_code, "GOL0000")

    def testUpdated(self):
        Flight.objects.filter(id=1).update(nm_destination=AirportCodes.GRU)
        voo = Flight.objects.get(tx_code="GOL0000")
        self.assertEqual(voo.nm_destination, str(AirportCodes.GRU.value))

    def testDeleted(self):
        sizeOrig = len(Flight.objects.all())
        Flight.objects.filter(id=1).delete()        
        sizeEnd = len(Flight.objects.all())
        self.assertEqual(sizeEnd, sizeOrig-1)

class FlightStatusCRUDTest(TestCase):
    def setUp(self):
        FlightStatus.objects.create(nm_status=Status.PREVISTO)

    def testCreated(self):
        status = FlightStatus.objects.get(nm_status=Status.PREVISTO)
        self.assertEqual(status.nm_status, str(Status.PREVISTO.value))

    def testUpdated(self):
        FlightStatus.objects.filter(id=1).update(nm_status=Status.EMBARCANDO)
        status = FlightStatus.objects.get(id=1)
        self.assertEqual(status.nm_status, str(Status.EMBARCANDO.value))

    def testDeleted(self):
        sizeOrig = len(FlightStatus.objects.all())
        FlightStatus.objects.filter(id=1).delete()        
        sizeEnd = len(FlightStatus.objects.all())
        self.assertEqual(sizeEnd, sizeOrig-1)

class UserCRUDTest(TestCase):
    def setUp(self):
        User.objects.create(tx_name="Izabela", nm_role=Role.GERENTE_DE_OPERACOES, tx_username="iza", tx_hash_key="905492")

    def testCreated(self):
        user = User.objects.get(tx_username="iza")
        self.assertEqual(user.tx_username, "iza")

    def testUpdated(self):
        User.objects.filter(id=1).update(tx_username="isa")
        user = User.objects.get(tx_name="Izabela")
        self.assertEqual(user.tx_username, "isa")

    def testDeleted(self):
        sizeOrig = len(User.objects.all())
        User.objects.filter(id=1).delete()        
        sizeEnd = len(User.objects.all())
        self.assertEqual(sizeEnd, sizeOrig-1)