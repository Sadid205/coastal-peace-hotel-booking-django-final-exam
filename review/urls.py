from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet
from django.urls import path,include
router = DefaultRouter()
router.register('list',ReviewViewSet)
urlpatterns = [
    path('',include(router.urls))
]
