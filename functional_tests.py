from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # This functional test was made so I could practive using the commands
    def test_can_edit_a_blog_post(self):
        self.fail('Already working, please remove this later')
        # Joseph needs to log in
        self.browser.get('http://127.0.0.1:8000/admin')
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('jdssdj1')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('Meggy')
        submitbox = self.browser.find_element_by_class_name('submit-row')
        submitbox.click()
        time.sleep(1)

        # Joseph wants to edit a blog post
        self.browser.get('http://127.0.0.1:8000/post/1/edit')

        # Joseph can see the title and header and knows it is his website
        self.assertIn('Joseph\'s Blog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Joseph\'s Blog', header_text)

        # Joseph can see where he needs to put the new title and text for the blog
        myclass = self.browser.find_element_by_class_name('col-md-8')
        mylabels = myclass.find_elements_by_tag_name('label')
        self.assertTrue(any(mylabel.text == 'Title:' for mylabel in mylabels))
        self.assertTrue(any(mylabel.text == 'Text:' for mylabel in mylabels))
        
        # Joseph makes a blog about greeting the world!
        inputbox = self.browser.find_element_by_id('id_title')
        inputbox.clear()
        inputbox.send_keys('Hello World!')

        # Joseph can see his title has updated as he typed
        self.assertTrue(inputbox,'Hello World!')

        # Joseph enters the lyrics to Hello by Adele to fill his blog post
        inputbox = self.browser.find_element_by_id('id_text')
        Adele = 'Hello, it\'s me. I was wondering if after all these years you\'d like to meet. To go over everything. They say that time\'s supposed to heal ya But I ain\'t done much healing Hello, can you hear me? I\'m in California dreaming about who we used to be When we were younger and free. I\'ve forgotten how it felt Before the world fell at our feet'
        inputbox.clear()
        inputbox.send_keys(Adele)

        # Joseph can see his text has updated as he typed
        self.assertTrue(inputbox,Adele)

        # Joseph can see where he needs to click to submit his post clearly
        submitbox = self.browser.find_element_by_tag_name('button')
        # buttonclass = self.browser.find_element_by_class_name('save btn btn-default')
        # self.assertEqual(buttonclass,'Save & Submit')

        # Joseph Saves and submits his post
        submitbox.click()
        time.sleep(1)

        # Joseph can see his blog post
        blog_name_text = self.browser.find_element_by_tag_name('h6').text  
        self.assertIn('Hello World!', blog_name_text)
        post_text = self.browser.find_element_by_class_name('post').text
        self.assertIn(Adele, post_text)

    def test_can_see_CV(self):
        # Edith wants to check out Joseph's CV
        self.browser.get('http://127.0.0.1:8000/cv')

        # She notices the page title and header show it is about Joseph's CV
        self.assertIn('Joseph\'s CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Joseph\'s CV', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')  

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)  

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        self.fail('Finish the test!')


#This is fine I think
if __name__ == '__main__':
        unittest.main(warnings='ignore')




# browser = webdriver.Firefox()
# assert 'Joseph\'s Blog' in browser.title, "Browser title was " + browser.title
# browser.quit()