"""This module defines a custom django-admin command for seeding the database"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from listings.models import Listing, User, Booking
from listings.serializers import ListingSerializer
from faker import Faker
import random


class Command(BaseCommand):
    """A custom command for seeding the database"""
    help = "A custom command for seeding the database"

    def add_arguments(self, parser):
        return super().add_arguments(parser)
    
    def handle(self, *args, **options):
        time = timezone.now().strftime("%X")
        self.stdout.write(self.style.SUCCESS(f"Seeding the database now.....{time}"))
        faker = Faker()
        # create random users
        for i in range(1, 6):
            try:
                User.objects.create_user(username=f"username{i}", email=faker.email(), password="password")
                User.objects.create_user(username=f"host{i}", email=faker.email(), password="password")
            except Exception as e:
                self.stderr.write(self.style.ERROR_OUTPUT(e.with_traceback(e.__traceback__)))
        # create random listings
        Listing.objects.all().delete()
        for i in range(1, 51):
            index = random.randint(1, 5)
            host = User.objects.get(username=f"host{index}")

            data = {
                "host": host,
                "name": f"fake_building_name{i}",
                "location": faker.street_address(),
                "description": faker.catch_phrase(),
                "price_per_night": random.randint(100, 1000)
            }

            try:
                Listing.objects.create(**data)
            except Exception as e:
                self.stderr.write(self.style.ERROR_OUTPUT(e.with_traceback(e.__traceback__)))
        # create random bookings
        Booking.objects.all().delete()
        all_listings = Listing.objects.all()[:]
        for _ in range(100):
            index = random.randint(1, 50)
            user_index = random.randint(1, 5)
            property = random.choice(all_listings)
            # property = Listing.objects.get(name=f"fake_building_name{index}")
            guest = User.objects.get(username=f"username{user_index}")

            data = {
                "property": property,
                "guest": guest,
                "start_date": faker.date(),
                "end_date": faker.future_date(),
                "total_price": (property.price_per_night * 5)
            }

            try:
                Booking.objects.create(**data)
            except Exception as e:
                self.stderr.write(self.style.ERROR_OUTPUT(e.with_traceback(e.__traceback__)))
        self.stdout.write(self.style.SUCCESS(f"Done {time}"))