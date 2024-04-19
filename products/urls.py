from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductListView,ProductDetailView

urlpatterns = [
    path('products/',ProductListView.as_view()),
    path('products/<int:pk>/',ProductDetailView.as_view(),name='product-detail')
]
