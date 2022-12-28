from django.contrib import admin
from .models import Reservation, Rental
# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "check_in", 'check_out',)

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ("name",)
