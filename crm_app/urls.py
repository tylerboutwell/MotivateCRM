from django.urls import path

from . import views

app_name = "crm_app"
urlpatterns = [
    path("", views.index, name="index"),

    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    path("recent_orders/", views.recent_orders_generic.as_view(), name="recent orders"),

    path("customer/<int:pk>/", views.CustomerDetailView.as_view(), name="customer detail")
]