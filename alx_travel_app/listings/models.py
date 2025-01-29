from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Listing(models.Model):
    property_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    host = models.ForeignKey(to=User, related_name="listings", related_query_name="property", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Booking(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", _("Booking is on pending",)
        CONFIRMED = "confirmed", _("Booking confirmed")
        CANCELED = "canceled", _("Booking canceled")


    booking_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    property = models.ForeignKey(to=Listing, related_name="bookings", related_query_name="booking", on_delete=models.CASCADE)
    guest = models.ForeignKey(to=User, related_name="bookings", related_query_name="booking", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=9, choices=Status, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["property", "start_date"],
                name="unique_booking_constraint",
                violation_error_message="a property can only be booked once for each start_date(check-in date)"
            )
        ]

    def __str__(self):
        return f'Booking:: {self.property.name} | {self.start_date.strftime("%d-%m-%y")} - {self.end_date.strftime("%d-%m-%y")}'


class Review(models.Model):
    review_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    listing = models.ForeignKey(to=Listing, related_name="reviews", related_query_name="review", on_delete=models.CASCADE)
    guest = models.ForeignKey(to=User, related_name="reviews", related_query_name="review", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1, rating__lte=5),
                name="valid_rating_constraint",
                violation_error_message="rating value must fall within 1 to 5"
            ),
            models.UniqueConstraint(
                fields=["guest", "listing"],
                name="unique_review_constraint",
                violation_error_message="A user can only review a property once"
            )
        ]
    
    def __str__(self):
        return f"{self.guest} - {self.property.name} | {self.rating}/5"
