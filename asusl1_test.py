from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
 	 
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000/AsusL1')

		compare_button = self.browser.find_element_by_id('btn1')
		compare_button.click()
		time.sleep(5)
		

		#self.assertTrue(any(row.text == '1: Gab'), "Wala ka pang table!")

if __name__ == '__main__':
	unittest.main(warnings='ignore')
