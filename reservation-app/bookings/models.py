from django.db import models

# Create your models here.
class Rental(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}: {self.name}"


class Reservation(models.Model):
    id = models.BigAutoField(primary_key=True)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.rental}: {self.check_in} - {self.check_out})"


# SELECT  rnt.name, rsv.id, rsv.check_in, rsv.check_out, lag(rsv.id, 1) OVER (
#     PARTITION BY rnt.id
#     ORDER BY rsv.id ASC
#   ) previous_reservation_id
# FROM bookings_reservation rsv
# LEFT JOIN bookings_rental rnt ON rnt.id = rsv.rental_id

# Reservation.objects.prefetch_related().annotate(previous_reservation_id=Window(expression=Lag('id', 1), partition_by=[F('rental_id')], order_by=F('id').asc() )).values('rental_id__name', 'id', 'check_in', 'check_out', 'previous_reservation_id')