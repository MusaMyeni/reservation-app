from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from bookings.models import Reservation
from django_tables2 import SingleTableMixin, SingleTableView
from .tables import ReservationTable
from django.db.models.functions import Lag
from django.db.models import Window, F 

# Create your views here.
class HomeView(LoginRequiredMixin, SingleTableView):
    queryset = Reservation.objects.prefetch_related().annotate(previous_reservation_id=Window(expression=Lag('id', 1), partition_by=[F('rental_id')], order_by=F('id').asc() )).values('rental__name', 'id', 'check_in', 'check_out', 'previous_reservation_id')
    table_class = ReservationTable
    template_name = "home.html"
