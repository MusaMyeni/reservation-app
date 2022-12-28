from django.test import TestCase
from django.db.models import Window, F
from django.db.models.functions import Lag
from bookings.models import Reservation, Rental
from datetime import date


class TestModels(TestCase):
    def test_rental(self):
        rental = Rental.objects.create(name="Vosrite Fishing Adventures")
        self.assertEquals(rental.id, 1)


    def test_reservation(self):
        rental = Rental.objects.create(name="Vosrite Fishing Adventures")
        check_in = date(2022, 10, 8)
        check_out = date(2022, 10, 16)
    
        resv = Reservation.objects.create(rental=rental, check_in=check_in, check_out=check_out)

        self.assertEquals(resv.id, 1)

    def test_reservation_previous_id(self):
        '''Testing to check setup Lag function properly gets the previous ID in the same object'''
        rental_1 = Rental.objects.create(name="Vosrite Fishing Adventures")
        rental_2 = Rental.objects.create(name="Rooiberg Nature Reserve")

        Reservation.objects.create(rental=rental_1, check_in=date(2022, 10, 8), check_out=date(2022, 10, 16))
        Reservation.objects.create(rental=rental_2, check_in=date(2022, 10, 8), check_out=date(2022, 10, 16))
        Reservation.objects.create(rental=rental_1, check_in=date(2022, 10, 18), check_out=date(2022, 10, 21))

        expected_second_row = {'rental_id__name': 'Vosrite Fishing Adventures', 'id': 3, 'check_in': date(2022, 10, 18), 'check_out': date(2022, 10, 21), 'previous_reservation_id': 1}

        query = Reservation.objects.annotate(previous_reservation_id=Window(expression=Lag('id', 1), partition_by=[F('rental_id')], order_by=F('id').asc() )).values('rental_id__name', 'id', 'check_in', 'check_out', 'previous_reservation_id')

        self.assertEquals(expected_second_row, query[1])


