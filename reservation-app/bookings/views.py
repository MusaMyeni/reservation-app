from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from bookings.models import Reservation

# Create your views here.
class HomeView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = "home.html"

