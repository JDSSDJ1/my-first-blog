from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from cv.views import cv_page, cv_edit
from blog.views import post_list
from cv.models import Section

class LoginTest(TestCase):
    # Make login class thing then cleanup or somethoing...

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

    def test_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv.html')
    
    def test_has_button_that_allows_edits(self):

        response = self.client.get('/cv/')
        html = response.content.decode('utf8')
        self.assertIn('href="/cv/edit/', html)
    
    def test_cv_page_uses_css(self):
        response = self.client.get('/cv/')
        html = response.content.decode('utf8')
        self.assertIn('<link rel="stylesheet', html.strip()) # doesn't check if commented
    
    def test_cv_sections_can_be_viewed(self):
        Section.objects.create(title='Activity 1', text='What I did')

        response = self.client.get('/cv/')

        self.assertIn('Activity 1', response.content.decode())
        self.assertIn('What I did', response.content.decode())

class CVEditTest(TestCase):
    
    def test_cv_edit_returns_correct_html(self):
        response = self.client.get('/cv/edit/')

        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>Joseph\'s CV</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'cv/cv_edit.html')
    
    def test_cv_section_can_be_viewed_to_edit(self):
        Section.objects.create(title='Activity 1', text='What I did')

        response = self.client.get('/cv/edit/')

        self.assertIn('Activity 1', response.content.decode())
        self.assertIn('What I did', response.content.decode())
















# class ItemModelTest(TestCase):

#     def test_saving_and_retrieving_items(self):
#         first_item = Item()
#         first_item.text = 'The first (ever) list item'
#         first_item.save()

#         second_item = Item()
#         second_item.text = 'Item the second'
#         second_item.save()

#         saved_items = Item.objects.all()
#         self.assertEqual(saved_items.count(), 2)

#         first_saved_item = saved_items[0]
#         second_saved_item = saved_items[1]
#         self.assertEqual(first_saved_item.text, 'The first (ever) list item')
#         self.assertEqual(second_saved_item.text, 'Item the second')

#     def test_only_saves_items_when_necessary(self):
#         self.client.get('/cv/')
#         self.assertEqual(Item.objects.count(), 0)



# class CVPageTest(TestCase):

#     def test_can_save_a_POST_request(self):
#         response = self.client.post('/cv/', data={'item_text': 'A new list item'})

#         self.assertEqual(Item.objects.count(), 1)  
#         new_item = Item.objects.first()  
#         self.assertEqual(new_item.text, 'A new list item')  

#     def test_redirects_after_POST(self):        
#         response = self.client.post('/cv/', data={'item_text': 'A new list item'})

#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response['location'], '/cv/')

#     def test_displays_all_list_items(self):
#         Item.objects.create(text='itemey 1')
#         Item.objects.create(text='itemey 2')

#         response = self.client.get('/cv/')

#         self.assertIn('itemey 1', response.content.decode())
#         self.assertIn('itemey 2', response.content.decode())