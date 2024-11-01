from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet,TransactionTotals
from django.urls import path,include
router = DefaultRouter()
router.register('list',TransactionViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('transaction-totals/',TransactionTotals,name='transactoin_totals'),
]
