from django.db.models.signals import post_save
from django.dispatch import receiver
from listings.models import Booking, Payment


@receiver(post_save, sender=Booking)
def initialize_payment(sender, instance: Booking, created, **kwargs):
    """Initialize payment once booking is created"""
    number_of_nights = (instance.end_date - instance.start_date).days
    totoal_price = number_of_nights * instance.property.price_per_night
    if created:
        Payment.objects.create(
            transaction_id=instance.pk,
            booking_id=instance,
            amount=totoal_price,
        )