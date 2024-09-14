from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.list_products, name="list-products"),
    path("products/create/", views.create_product, name="create-product"),
]
