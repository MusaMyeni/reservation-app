from django.test import TestCase
from bookings.forms import ReservationForm
from bookings.models import Reservation, Rental
from django.forms import ValidationError

class TestForms(TestCase):
    
    def setUp(self):
        self.rental_1 = Rental.objects.create(name='Zebula Game Lodge')

    def test_reservation_form_valid_data(self):
        '''Testing form validity when using correct data'''
        form = ReservationForm(data={
            'rental': self.rental_1,
            'check_in': '2022-10-01',
            'check_out': '2022-10-08'
        })

        self.assertTrue(form.is_valid())

    def test_reservation_form_no_data(self):
        '''Testing form validity when using incorrect data'''
        form = ReservationForm(data={})
        self.assertGreater(len(form.errors), 1)


    def test_reservation_form_timeslot_overlap(self):
        '''Testing form validity if another reservation exists within a desired timeframe'''
        form = ReservationForm(data={
            'rental': self.rental_1,
            'check_in': '2022-10-01',
            'check_out': '2022-10-08'
        })
        form.save()

        form_2 = ReservationForm(data={
            'rental': self.rental_1,
            'check_in': '2022-10-08',
            'check_out': '2022-10-10'
        })

        form_3 = ReservationForm(data={
            'rental': self.rental_1,
            'check_in': '2022-09-28',
            'check_out': '2022-10-01'
        })

        self.assertFalse(form_2.is_valid())
        self.assertFalse(form_3.is_valid())




