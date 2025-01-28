from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import GatewayView, PaymentView

urlpatterns = [
    path('gateways/', GatewayView.as_view()),
    path('pay/', PaymentView.as_view())

]
