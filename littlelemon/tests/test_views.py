# from django.test import TestCase
# from django.http import HttpRequest

# from restaurant.models import Menu
# from restaurant.views import MenuItemsView
# from restaurant.serializers import MenuSerializer

# class MenuViewTest(TestCase):
#     def setup(self):
#         Menu.objects.create(title='IceCream',price=80,inventory=100)
#         Menu.objects.create(title='Pizza',price=100,inventory=50)

#     def test_getall(self):
#         menu_items = Menu.objects.all()
#         menu_items_serialized = MenuSerializer(menu_items)
#         request = HttpRequest()
#         response = MenuItemsView.get(self, request)
#         self.assertEquals(response, menu_items_serialized)
