from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import BookingForm
from travel_options.models import TravelOption
from .models import Booking

# Create your views here.
@login_required
def booking_form(request, pk):
    travel_option = get_object_or_404(TravelOption, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST, available_seats=travel_option.available_seats)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.travel_option = travel_option
            booking.save()
        return redirect("my_bookings")
    else:
        form = BookingForm(available_seats=travel_option.available_seats)
    return render(request, "bookings/booking_form.html", {"travel_option": travel_option})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if booking.status == "X":
        messages.info(request, "This booking is already cancelled.")
    else:
        booking.status = "X"
        booking.save()
        booking.travel_option.available_seats += booking.number_of_seats
        booking.travel_option.save()
        messages.success(request, "Your booking has been cancelled successfully.")

    return redirect("my_bookings")