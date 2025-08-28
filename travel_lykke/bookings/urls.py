from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/book/', views.booking_form, name="booking_form"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path("cancel-booking/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
]