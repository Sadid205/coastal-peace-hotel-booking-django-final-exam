from django.urls import path,include
from .views import BookingViewSet,HotelBookingViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('list',BookingViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('<int:hotel_id>/',HotelBookingViewSet.as_view(),name="hotel_booking")
]
