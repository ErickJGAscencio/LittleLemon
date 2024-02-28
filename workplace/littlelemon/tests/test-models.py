from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from restaurant.api.models import MenuItem, Menu
from restaurant.api.serializers import MenuSerializer

class MenuItemTest(TestCase):
  def test_get_item(self):
    item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
    self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        # Add a few test instances of the Menu model
        Menu.objects.create(title='Pizza', price=12.99, inventory=20)
        Menu.objects.create(title='Salad', price=8.99, inventory=30)
        Menu.objects.create(title='Pasta', price=10.99, inventory=25)

    def test_getall(self):
        # Retrieve all the Menu objects added for the test purpose
        client = APIClient()
        url = reverse('menu-list')
        response = client.get(url)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the retrievedd objects
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)
