# DRF
# from rest_framework import routers
from django.urls import path, include
from shared.rest_framework.router import OptionalSlashRouter

# Projects
from calculator.views import CreditViewSet, PaymentViewSet, calculate

router = OptionalSlashRouter()

router.register('credit', CreditViewSet, 'credit')
router.register('payment', PaymentViewSet, 'payment')

urlpatterns = [
    path('', include(router.urls)),
    path('calculating/', calculate, name='calculate'),
]
