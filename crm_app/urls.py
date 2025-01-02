from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("<int:transaction_id>/", views.detail, name="detail"),

    path("recent_orders/", views.recent_orders, name="recent orders")
]