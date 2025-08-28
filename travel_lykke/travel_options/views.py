from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TravelOption

# Create your views here.

def travel_options(request):
    options = TravelOption.objects.all()
    return render(request, 'travel_options/travel_options.html', {"travel_options": options})

def travel_option_details(request, pk):
    option = get_object_or_404(TravelOption, pk=pk)
    return render(request, "travel_options/details.html", {"option": option})