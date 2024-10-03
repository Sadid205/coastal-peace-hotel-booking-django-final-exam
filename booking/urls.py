from django.urls import path,include
from .views import BookingViewSet,HotelBookingViewSet,PendingBooking,ConfirmBookingView,CancelBookingView,BookingInfoView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('list',BookingViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('<int:hotel_id>/',HotelBookingViewSet.as_view(),name="hotel_booking"),
    path('pending_booking/',PendingBooking.as_view(),name="pending_booking"),
    path('confirm_booking/<int:booking_id>/',ConfirmBookingView.as_view(),name="confirm_booking"),
    path('cancel_booking/<int:booking_id>/',CancelBookingView.as_view(),name="cancle_booking"),
    path('booking_info/',BookingInfoView.as_view(),name="booking_info"),
]
