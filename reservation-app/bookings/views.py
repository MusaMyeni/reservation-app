from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReservationForm
from django.views.generic import CreateView
from bookings.models import Reservation
from django_tables2 import SingleTableView
from .tables import ReservationTable
from django.db.models.functions import Lag
from django.db.models import Window, F 
from django.urls import reverse_lazy


# Create your views here.
class HomeView(LoginRequiredMixin, SingleTableView):
    queryset = Reservation.objects.prefetch_related().annotate(previous_reservation_id=Window(expression=Lag('id', 1), partition_by=[F('rental_id')], order_by=F('id').asc() )).values('rental__name', 'id', 'check_in', 'check_out', 'previous_reservation_id')
    table_class = ReservationTable
    template_name = "home.html"

class CreateReservationView(LoginRequiredMixin, CreateView):
    form_class = ReservationForm
    template_name = "create-reservation.html"
    success_url=reverse_lazy("home")
