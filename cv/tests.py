from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from cv.views import cv_page
from blog.views import post_list

class HomePageTest(TestCase):

    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)


class CVPageTest(TestCase):

    def test_cv_page_returns_correct_html(self):
        response = self.client.get('/cv/')

        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>Joseph\'s CV</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'cv/cv.html')

