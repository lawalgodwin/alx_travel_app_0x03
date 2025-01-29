from django.shortcuts import render
from rest_framework import viewsets
from .models import Booking, Listing
from .serializers import BookingSerializer, ListingSerializer
from listings.tasks import send_booking_confirmation


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            send_booking_confirmation.delay()
        return super().create(request, *args, **kwargs)
