from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductListView

urlpatterns = [
    path('products/',ProductListView.as_view())
]
