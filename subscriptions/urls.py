from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PackageView, SubscriptionView

urlpatterns = [
    path('packages/',PackageView.as_view()),
    path('subscriptions/',SubscriptionView.as_view()),

]