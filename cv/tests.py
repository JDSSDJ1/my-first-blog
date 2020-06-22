from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from cv.views import cv_page
from blog.views import post_list

class HomePageTest(TestCase):

    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    # def test_post_list_returns_correct_html(self):
    #     request = HttpRequest()  
    #     response = cv_page(request)  
    #     html = response.content.decode('utf8')  
    #     self.assertTrue(html.startswith('<html>'))  
    #     self.assertIn('<title>Joseph\'s Blog</title>', html)  
    #     self.assertTrue(html.endswith('</html>'))


class CVPageTest(TestCase):
    def test_cv_page_returns_correct_html(self):
        request = HttpRequest()  
        response = cv_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>Joseph\'s CV</title>', html)  
        self.assertTrue(html.endswith('</html>'))
#     def test_root_url_resolves_to_cv_page_view(self):
#         found = resolve('cv/')
#         self.assertEqual(found.func, cv_page)


# Create your tests here.

# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.asserEqual(1 + 1, 3)