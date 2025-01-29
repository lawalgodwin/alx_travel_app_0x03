from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings



@shared_task(name="send_booking_confirmation", countdown=20)
def send_booking_confirmation():
    """A task that sends booking confirmation mail"""
    send_mail(
        auth_user=settings.EMAIL_HOST_USER,
        auth_password=settings.EMAIL_HOST_PASSWORD,
        subject="Test Email fuctionality with Django",
        message="This is the body of the message",
        from_email="godwinl200@gmail.com",
        recipient_list=["godwin.lawal.dev@gmail.com"],
        fail_silently=False
    )