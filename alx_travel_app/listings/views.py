import hashlib
from django.http import Http404
import requests
import json
import uuid
import hmac
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.conf import settings
from rest_framework.views import APIView
from .models import Booking, Listing, Payment
from .serializers import BookingSerializer, ListingSerializer, PaymentSerializer
from .tasks import confirm_booking


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class PaymentInitializationView(APIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def post(self, request, booking_id):
        # get booking details from the request object
        booking = None
        total_price = 0
        try:
            booking = get_object_or_404(Booking, pk=booking_id)
            number_of_nights = (booking.end_date - booking.start_date).days
            total_price = number_of_nights * booking.property.price_per_night
        except Http404 as e:
            return Response("Booking not found", status=status.HTTP_404_NOT_FOUND)
        # prepare chapa api payload
        url = "https://api.chapa.co/v1/transaction/initialize"
        payload = {
        "amount": f"{total_price}",
        "currency": "ETB",
        "email": "abebech_bekele@gmail.com",
        "first_name": "Bilen",
        "last_name": "Gizachew",
        "phone_number": "0912345678",
        "tx_ref": str(booking.pk),
        "return_url": "https://www.myfrontend.com/",
        "customization": {
        "title": "Booking",
        "description": "Payment for Apartment Booking"
        }
        }
        headers = {
        'Authorization': f'Bearer {settings.CHAPA_SECRET_KEY}',
        'Content-Type': 'application/json'
        }
        
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == status.HTTP_200_OK:
            data = response.json()
            return Response(data.get("data")["checkout_url"])
        return Response("Unable to process your request")


class ChapaWebhookView(APIView):
    """Handling Webhook events"""
    # swagger_schema = None

    def post(self, request, *args, **kwargs):
        print("Webhook reached")
        event = json.loads(request.body)
        chapa_signature = request.headers.get("Chapa-Signature")
        if not chapa_signature:
            return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
        hash_secret_key = settings.CHAPA_WEBHOOK_SECRET
        signature = hmac.new(hash_secret_key.encode(), hash_secret_key.encode(), hashlib.sha256).hexdigest()
        if not (signature==chapa_signature):
            return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
        # On successful payment, send a confirmation email to the user (using Celery for background tasks)
        if event.get("status") == "success":
            confirm_booking.delay(event.get("email"), event.get("status"))
            transaction_id = event.get("tx_ref")
            payment = Payment.objects.get(transaction_id=transaction_id)
            payment.status = Payment.Status.COMPLETED
            payment.save()
        # Handle any errors or payment failures gracefully, updating the status in the Payment model accordingly.
        if event.get("failure_reason"):
            confirm_booking.delay(event.get("email"), event.get("status"))
        return Response(status=200)