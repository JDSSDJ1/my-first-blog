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
        # self.fail('Test complete and should remain working')

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

    def test_can_view_cv(self):
        self.browser.get('http://127.0.0.1:8000/cv')
        # Joseph can see the title and header and knows it is his website and his CV
        self.assertIn('Joseph\'s CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Joseph\'s CV', header_text)

        thisSection = self.browser.find_elements_by_class_name('section')

        self.assertTrue(len(thisSection) >= 1)

    def test_can_edit_cv(self):
        # Joseph cannot edit the page without logging in
        self.browser.get('http://127.0.0.1:8000/cv/edit')
        
        submitNo = len(self.browser.find_elements_by_tag_name('button')) - 1
        submitbox = self.browser.find_elements_by_tag_name('button')[submitNo]
        submitbox.click()
        time.sleep(1)
        self.assertIn('ValueError', self.browser.title)

        # Joseph Needs to Log in to edit the sections
        self.browser.get('http://127.0.0.1:8000/admin')
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('jdssdj1')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('Meggy')
        submitbox = self.browser.find_element_by_class_name('submit-row')
        submitbox.click()
        time.sleep(1)

        # Joseph should now be able to edit his cv
        self.browser.get('http://127.0.0.1:8000/cv/edit')
        time.sleep(1)

        # Joseph Updates the first section on his CV
        # thisSection = self.browser.find_elements_by_class_name('section-form')
        theTitle = self.browser.find_elements_by_id('id_title')[0]
        theTitle.clear()
        theTitle.send_keys('Hello World!')

        theText = self.browser.find_elements_by_id('id_text')[0]
        theText.clear()
        theText.send_keys("Testing 1, 2, 3")

        # Joseph Updates the second section on his CV
        theTitle = self.browser.find_elements_by_id('id_title')[1]
        theTitle.clear()
        theTitle.send_keys('This is another Test')

        theText = self.browser.find_elements_by_id('id_text')[1]
        theText.clear()
        theText.send_keys("Testing 4, 5, 6")

        submitbox = self.browser.find_elements_by_tag_name('button')[submitNo]
        submitbox.click()

        self.browser.get('http://127.0.0.1:8000/cv/')
        # Joseph Checks his cv was updated correctly
        thisSection = self.browser.find_elements_by_class_name('section')
        theTitle = thisSection[0].find_element_by_tag_name('h2').text
        theText = thisSection[0].find_element_by_tag_name('p').text

        self.assertIn('Hello World!', theTitle)
        self.assertIn('Testing 1, 2, 3', theText)

        theTitle = thisSection[1].find_element_by_tag_name('h2').text
        theText = thisSection[1].find_element_by_tag_name('p').text

        self.assertIn('This is another Test', theTitle)
        self.assertIn('Testing 4, 5, 6', theText)

    def test_can_i_create_new_section(self):
        # Joseph counts the number of sections on the page
        self.browser.get('http://127.0.0.1:8000/cv')
        noOfSections = len(self.browser.find_elements_by_class_name('section'))

        # Joseph cannot add to the page without logging in
        self.browser.get('http://127.0.0.1:8000/cv/edit')
        submitNo = len(self.browser.find_elements_by_tag_name('button')) - 1
        submitbox = self.browser.find_elements_by_tag_name('button')[submitNo]
        submitbox.click()
        time.sleep(1)

        self.assertIn('ValueError', self.browser.title)

        # Joseph Needs to Log in to add to the page
        self.browser.get('http://127.0.0.1:8000/admin')
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('jdssdj1')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('Meggy')
        submitbox = self.browser.find_element_by_class_name('submit-row')
        submitbox.click()
        time.sleep(1)

        # Joseph should now be able to add to his cv
        self.browser.get('http://127.0.0.1:8000/cv/edit')
        time.sleep(1)

        # Joseph clicks the button that enables him to add another section
        addbox = self.browser.find_elements_by_tag_name('button')[0]
        addbox.click()
        time.sleep(1)
        submitNo = submitNo + 1

        # Joseph Writes in to the new title and text
        final = len(self.browser.find_elements_by_id('id_title')) - 1
        theTitle = self.browser.find_elements_by_id('id_title')[final]
        theTitle.clear()
        theTitle.send_keys('On the End')

        theText = self.browser.find_elements_by_id('id_text')[final]
        theText.clear()
        theText.send_keys("We add this")

        # Joseph submits the new section to be saved
        submitbox = self.browser.find_elements_by_tag_name('button')[submitNo]
        submitbox.click()
        time.sleep(1)

        self.browser.get('http://127.0.0.1:8000/cv/')
        # Joseph checks the new section did save
        thisSection = self.browser.find_elements_by_class_name('section')
        theTitle = thisSection[final].find_element_by_tag_name('h2').text
        theText = thisSection[final].find_element_by_tag_name('p').text

        self.assertIn('On the End', theTitle)
        self.assertIn("We add this", theText)
        self.assertTrue(len(thisSection) == noOfSections + 1)

    def test_can_I_delete_sections(self):

        # Joseph counts the number of sections on the page
        self.browser.get('http://127.0.0.1:8000/cv')
        noOfSections = len(self.browser.find_elements_by_class_name('section'))

        # Joseph cannot remove from the page without logging in
        self.browser.get('http://127.0.0.1:8000/cv/edit')
        submitNo = len(self.browser.find_elements_by_tag_name('button')) - 1
        submitbox = self.browser.find_elements_by_tag_name('button')[submitNo]
        submitbox.click()
        time.sleep(1)

        self.assertIn('ValueError', self.browser.title)

        # Joseph Needs to Log in to remove from the page
        self.browser.get('http://127.0.0.1:8000/admin')
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('jdssdj1')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('Meggy')
        submitbox = self.browser.find_element_by_class_name('submit-row')
        submitbox.click()
        time.sleep(1)

        # Joseph should now be able to remove from his cv
        self.browser.get('http://127.0.0.1:8000/cv/edit')
        time.sleep(1)

        #Joseph removes the section with number listed below, he reads it to check it has gone
        deletedSection = 1
        theTitle = self.browser.find_elements_by_id('id_title')[deletedSection]
        theText = self.browser.find_elements_by_id('id_text')[deletedSection]
        theButton = self.browser.find_elements_by_tag_name('button')[deletedSection + 1]
        theButton.click()
        time.sleep(1)

        # Joseph checks the main CV page for changes
        self.browser.get('http://127.0.0.1:8000/cv')

        # Joseph counts the total sections to compare to the original total and sees whether there are less sections
        thisSection = self.browser.find_elements_by_class_name('section')
        self.assertTrue(len(thisSection) == noOfSections - 1)

        # Joseph looks at the text to make sure the section has gone
        theTitle2 = thisSection[deletedSection].find_element_by_tag_name('h2').text
        theText2 = thisSection[deletedSection].find_element_by_tag_name('p').text
        self.assertTrue(theTitle != theTitle2)
        self.assertTrue(theText != theText2)


    # def check_for_row_in_list_table(self, row_text):
    #     table = self.browser.find_element_by_id('id_list_table')
    #     rows = table.find_elements_by_tag_name('tr')
    #     self.assertIn(row_text, [row.text for row in rows])

    # def test_can_see_CV(self):
    #     # Edith wants to check out Joseph's CV
    #     self.browser.get('http://127.0.0.1:8000/cv')

    #     # She notices the page title and header show it is about Joseph's CV
    #     self.assertIn('Joseph\'s CV', self.browser.title)
    #     header_text = self.browser.find_element_by_tag_name('h1').text  
    #     self.assertIn('Joseph\'s CV', header_text)

    #     # She is invited to enter a to-do item straight away
    #     inputbox = self.browser.find_element_by_id('id_new_item')  
    #     self.assertEqual(
    #         inputbox.get_attribute('placeholder'),
    #         'Enter a to-do item'
    #     )

    #     # She types "Buy peacock feathers" into a text box (Edith's hobby
    #     # is tying fly-fishing lures)
    #     inputbox.send_keys('Buy peacock feathers')  

    #     # When she hits enter, the page updates, and now the page lists
    #     # "1: Buy peacock feathers" as an item in a to-do list table
    #     inputbox.send_keys(Keys.ENTER)  
    #     time.sleep(1)  
    #     self.check_for_row_in_list_table('1: Buy peacock feathers')
    
    #     # There is still a text box inviting her to add another item. She
    #     # enters "Use peacock feathers to make a fly" (Edith is very
    #     # methodical)
    #     inputbox = self.browser.find_element_by_id('id_new_item')
    #     inputbox.send_keys('Use peacock feathers to make a fly')
    #     inputbox.send_keys(Keys.ENTER)
    #     time.sleep(1)

    #     # The page updates again, and now shows both items on her list
    #     self.check_for_row_in_list_table('1: Buy peacock feathers')
    #     self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


    #     self.fail('Finish the test!')








if __name__ == '__main__':
        unittest.main(warnings='ignore')
