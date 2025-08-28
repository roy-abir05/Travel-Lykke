from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_options, name='travel_options'),
    path('<int:pk>/', views.travel_option_details, name='travel_option_details'),
]