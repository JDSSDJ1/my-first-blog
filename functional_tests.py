from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_blog_posts(self):
        # Edith heard about a blog by Joseph so check it out
        self.browser.get('http://127.0.0.1:8000')

        # Edith can see the title and header and it is about Joseph's Blog
        self.assertIn('Joseph\'s Blog', self.browser.title)

        self.fail('Finish the test!')


if __name__ == '__main__':
        unittest.main(warnings='ignore')




# browser = webdriver.Firefox()
# assert 'Joseph\'s Blog' in browser.title, "Browser title was " + browser.title
# browser.quit()