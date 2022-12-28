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
