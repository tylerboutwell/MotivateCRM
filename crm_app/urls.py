from django.urls import path

from .views import views, user_views

app_name = "crm_app"
urlpatterns = [
    path("", user_views.home, name="home"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("transactions/", views.transactions.as_view(), name="transactions"),
    path("add_transaction", views.AddTransaction, name= "add transaction"),
    path("customers/", views.Customers, name="customers"),
    path("customer/<int:pk>/", views.CustomerView, name="customer detail"),
    path("add_customer", views.AddCustomer, name= "add customer"),
    path("delete_customer/<int:pk>/", views.DeleteCustomer, name = "delete customer"),
    path("delete_transaction/<int:pk>/", views.DeleteTransaction, name="delete transaction"),
    path("customer/<int:pk>/transactions", views.CustomerTransactionsView, name="customer transactions"),
    path("transaction/<int:pk>/", views.TransactionView, name="transaction detail"),
    path("logout/", user_views.logout_user, name="logout"),
    path("customer/<int:pk>/update/", views.UpdateCustomerView, name="update customer")
]