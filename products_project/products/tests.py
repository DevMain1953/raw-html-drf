from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product


class ProductAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": 10.99,
        }

    def test_get_products(self):
        Product.objects.create(
            name="Sample Product", description="Sample Description", price=9.99
        )
        response = self.client.get(reverse("list-products"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Sample Product")

    def test_create_product(self):
        response = self.client.post(
            reverse("create-product"), self.product_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.first().name, "Test Product")
