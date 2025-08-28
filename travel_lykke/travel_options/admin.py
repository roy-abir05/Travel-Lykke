from django.contrib import admin
from .models import TravelOption

# Register your models here.
@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ('travel_id', 'type', 'source', 'destination', 'departure_time', 'arrival_time', 'price', 'available_seats')