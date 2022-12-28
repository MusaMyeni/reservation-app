
from .models import Reservation
import django_tables2 as tables

class ReservationTable(tables.Table):
    class Meta:
        model = Reservation
        fields = ('rental__name', 'id', 'check_in', 'check_out', 'previous_reservation_id')
        template_name = "table.html"