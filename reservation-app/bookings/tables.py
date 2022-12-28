
from .models import Reservation
import django_tables2 as tables

class ReservationTable(tables.Table):
    class Meta:
        exclude = ('id', )
        model = Reservation
        template_name = "table.html"