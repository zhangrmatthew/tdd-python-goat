from urllib import request
from django.test import TestCase
from django.urls import resolve
from . import views
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item
#from lists.views import home_page 
#how does python resolve imports...from what directory, and importing across packages

# Create your tests here.
# class SmokeTest(TestCase):
#     def test_bad_intentional(self):
#         self.assertEqual(1 + 1, 3)

class HomePageTests(TestCase):

    # tests if the right view is sent
    def test_homepage_resolver(self):
        homepage = resolve("/")
        self.assertEqual(homepage.func, views.home_page)

    # tests if the right template was sent
    def test_homepage_content(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_POST_request(self):
        # post request contains the form data we wish to send
        response = self.client.post("/", data = {'item_text' : 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new list item")

        # self.assertIn("A new list item", response.content.decode())
        # self.assertTemplateUsed(response, "home.html"

    def test_redirects_after_POST(self):
        response = self.client.post("/", data = {'item_text' : 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], "/")

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(second_saved_item.text, "Item the second")

