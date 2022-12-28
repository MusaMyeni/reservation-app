from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from bookings.models import Reservation
from django_tables2 import SingleTableMixin
from .tables import ReservationTable

# Create your views here.
class HomeView(LoginRequiredMixin, SingleTableMixin, ListView):
    model = Reservation
    table_class = ReservationTable
    template_name = "home.html"

