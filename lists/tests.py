from urllib import request
from django.test import TestCase
from django.urls import resolve
from . import views
from django.http import HttpRequest
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
        request = HttpRequest()
        response = views.home_page(request)
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>To-Do Lists</title>", html)
        self.assertTrue(html.endswith("</html>"))

