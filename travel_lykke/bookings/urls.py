from django.urls import path
from . import views

urlpatterns = [
    path('<int:option_id>/book/', views.booking_form, name="booking_form"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
]