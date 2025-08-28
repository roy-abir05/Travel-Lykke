from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking

# Create your views here.
@login_required
def booking_form(request, option_id):
    # later you can fetch the travel option by ID and price
    # for now, just hardcode the price
    context = {"price": 258}
    if request.method == "POST":
        # process form submission here
        # e.g. save booking to DB
        return redirect("my_bookings")
    return render(request, "bookings/booking_form.html", context)

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})