from django.urls import path

from . import views

app_name = "crm_app"
urlpatterns = [
    path("", views.index, name="index"),

    path("<int:transaction_id>/", views.detail, name="detail"),

    path("recent_orders/", views.recent_orders, name="recent orders"),

    path("customer/<int:pk>/", views.DetailView.as_view(), name="customer detail")
]