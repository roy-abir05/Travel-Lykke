from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from travel_options.models import TravelOption


# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = [
        ('C', 'Confirmed'),
        ('X', 'Cancelled'),
    ]

    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='C')

    class Meta:
        indexes = [
            models.Index(fields=["user", "travel_option", "booking_date", "status"]),
        ]

    def save(self, *args, **kwargs):
        if self.pk is not None and self.status != 'X': # If updating an existing booking and status is not 'X'
            raise ValidationError("Existing bookings cannot be modified")
        if self.pk is None and self.status == 'X': # If creating a new booking and status is 'X'
            raise ValidationError("Cannot create a booking with status 'Cancelled'.")
        if self.status == 'C':
            try:
                self.travel_option.book_seats(self.number_of_seats)
                self.total_price = self.number_of_seats * self.travel_option.price
            except Exception as e:
                raise ValidationError(f"Cannot book seats:\n{e}")
        super().save(*args, **kwargs)

    def cancel_booking(self):
        if self.status == "X":
            raise ValidationError("Booking is already cancelled.")
        self.status = "X"
        self.travel_option.release_seats(self.number_of_seats)
        self.save()

    def __str__(self):
        return f"Booking {self.booking_id} - {self.user.username} - {self.travel_option}"