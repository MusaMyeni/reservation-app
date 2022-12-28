from django.forms import ModelForm, DateField, DateInput, ValidationError
from .models import Reservation
from django.db.models import Q

class ReservationForm(ModelForm):
    check_in = DateField(required=True, widget=DateInput(attrs={'type': 'date'}))
    check_out = DateField(required=True, widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Reservation
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'class': 'bg-white rounded-lg font-light font-montserrat text-center focus:ring-0 h-14 mb-8 w-full'})

    def clean(self):
        '''
            Adding checks to see if the checkout date is after the checkin date
            Checking to see if the rental is already booked out within the required period of time
        '''
        cleaned_data = super().clean()
        rental = cleaned_data['rental']
        check_in = cleaned_data['check_in']
        check_out = cleaned_data['check_out']
        is_booked = Reservation.objects.filter(Q(rental=rental) ,Q(check_in__range=[check_in, check_out]) | Q(check_out__range=[check_in, check_out])).exists()

        if is_booked:
            raise ValidationError(("The desired timeslots for that location overlaps with another booking."), code='invalid')

        if check_in > check_out:
            raise ValidationError(("Check in date cannot be after checkout date."), code='invalid')

