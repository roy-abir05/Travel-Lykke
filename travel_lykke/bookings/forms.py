from django import forms
from django.core.validators import MaxValueValidator
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_seats']

    def __init__(self, *args, available_seats=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['number_of_seats'].widget.attrs.update({
            'class': 'form-input h-14 p-4',
            'id': 'number-of-seats',
            'name': 'number_of_seats',
            'type': 'number',
            'required': True,
            'value': 1,
            'min': 1,
        })

        if available_seats is not None:
            self.fields['number_of_seats'].validators.append(
                MaxValueValidator(available_seats)
            )