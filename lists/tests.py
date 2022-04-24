from urllib import request
from django.test import TestCase
from django.urls import resolve
from . import views
from django.http import HttpRequest
from django.template.loader import render_to_string
#from lists.views import home_page 
#how does python resolve imports...from what directory, and importing across packages

# Create your tests here.
# class SmokeTest(TestCase):
#     def test_bad_intentional(self):
#         self.assertEqual(1 + 1, 3)

class HomePageTests(TestCase):

    def test_homepage_resolver(self):
        homepage = resolve("/")
        self.assertEqual(homepage.func, views.home_page)

    def test_homepage_content(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "home.html")

