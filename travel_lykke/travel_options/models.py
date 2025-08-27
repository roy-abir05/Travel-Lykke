from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class TravelOption(models.Model):
    
    TRAVEL_TYPES = [
        ('F', 'Flight'),
        ('T', 'Train'),
        ('B', 'Bus'),
    ]

    travel_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=1, choices=TRAVEL_TYPES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    class Meta:
        indexes = [
            models.Index(fields=["type", "source", "destination", "departure_time", "price"]),
        ]

    def book_seats(self, num_seats: int):
        if num_seats <= 0:
            raise ValidationError("Number of seats to book must be positive")
        if self.available_seats < num_seats:
            raise ValidationError("Not enough seats available")            
        self.available_seats -= num_seats
        self.save()
    
    def release_seats(self, num_seats: int):
        if num_seats <= 0:
            raise ValidationError("Number of seats to release must be positive")
        self.available_seats += num_seats
        self.save()


        
    def clean(self):
        if self.arrival_time <= self.departure_time:
            raise ValidationError("Arrival time must be after departure time.")
        if self.available_seats <= 0:
            raise ValidationError("Available seats must be greater than 0.")

    def __str__(self):
        return f"{self.type} {self.source} → {self.destination} ({self.departure_time} - {self.arrival_time})"
