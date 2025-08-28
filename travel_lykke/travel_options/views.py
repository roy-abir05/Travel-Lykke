from django.shortcuts import render, get_object_or_404
from django.utils.dateparse import parse_date
from .models import TravelOption

# Create your views here.

def travel_options(request):
    options = TravelOption.objects.all()

    travel_type = request.GET.getlist("type")
    source = request.GET.get("source", "").strip()
    destination = request.GET.get("destination", "").strip()
    date = request.GET.get("date", "").strip()

    if travel_type:
        options = options.filter(type__in=travel_type)

    if source:
        options = options.filter(source__icontains=source)

    if destination:
        options = options.filter(destination__icontains=destination)

    if date:
        parsed_date = parse_date(date)
        if parsed_date:
            options = options.filter(departure_time__date=parsed_date)

    return render(request, 'travel_options/travel_options.html', {"travel_options": options})

def travel_option_details(request, pk):
    option = get_object_or_404(TravelOption, pk=pk)
    tax = 10
    setattr(option, "taxes", tax)
    setattr(option, "base_fare", option.price - tax)
    return render(request, "travel_options/details.html", {"option": option})