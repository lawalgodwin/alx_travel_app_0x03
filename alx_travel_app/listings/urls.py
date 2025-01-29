from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"listings", viewset=ListingViewSet)
router.register(r"bookings", viewset=BookingViewSet)


urlpatterns = [
    path("", include(router.urls))
]
