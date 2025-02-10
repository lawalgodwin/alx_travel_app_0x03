from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(name="Devide numbers")
def divide(a, c):
    return (a / c)

@shared_task(name="Send Booking confirmation email")
def confirm_booking(email, status):
    """A task that sends booking confirmation mail"""
    send_mail(
        auth_user=settings.EMAIL_HOST_USER,
        auth_password=settings.EMAIL_HOST_PASSWORD,
        subject="Test Email fuctionality with Django",
        message=f"Payment status: {status}",
        from_email="godwinl200@gmail.com",
        recipient_list=[email],
        fail_silently=False
    )