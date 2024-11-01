from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import SpecialOfferView
router = DefaultRouter()

router.register('list',SpecialOfferView)
urlpatterns = [
    path('',include(router.urls))
]