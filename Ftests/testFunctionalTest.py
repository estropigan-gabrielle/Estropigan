from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time


class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	#def tearDown(self):
		#self.browser.quit()
	
	def test_start_list_and_retrieve(self):

		# BROWSER, TITLE, AND HEADER
		self.browser.get(self.live_server_url)
		self.assertIn('TMTK', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Us', headerText)

		# INQUIRY TYPE
		a9 = self.browser.find_element_by_xpath('/html/body/form/fieldset[1]/input[1]')
		a9.click()

		# PERSONAL INFORMATION

		# FIRST NAME
		a1 = self.browser.find_element_by_id('cu1')
		self.assertEqual(a1.get_attribute('placeholder'),'Your First Name')
		a1.send_keys('Gabrielle')
		time.sleep(1)

		# LAST NAME
		a2 = self.browser.find_element_by_id('cu2')
		self.assertEqual(a2.get_attribute('placeholder'),'Your Last Name')
		a2.send_keys('Estropigan')
		time.sleep(1)

		# AGE
		a3 = self.browser.find_element_by_id('cu3')
		self.assertEqual(a3.get_attribute('placeholder'),'Your Age')
		a3.send_keys('20')
		time.sleep(1)

		# EMAIL ADDRESS
		a4 = self.browser.find_element_by_id('cu4')
		self.assertEqual(a4.get_attribute('placeholder'),'Your E-mail Address')
		a4.send_keys('gstrpgn@gmail.com')
		time.sleep(1)

		# CELLPHONE NUMBER
		a5 = self.browser.find_element_by_id('cu5')
		self.assertEqual(a5.get_attribute('placeholder'),'Your Cellphone Number')
		a5.send_keys('09563207021')
		time.sleep(1)

		# ORGANIZATION
		a6= self.browser.find_element_by_id('cu6')
		self.assertEqual(a6.get_attribute('placeholder'),'Organization')
		selecta6 = Select(a6)
		selecta6.select_by_visible_text('OFFICE')
		time.sleep(1)

		# NAME OF ORGANIZATION
		a7 = self.browser.find_element_by_id('cu7')
		self.assertEqual(a7.get_attribute('placeholder'),'Enter Name of Organization')
		a7.send_keys('USG')
		time.sleep(1)

		# MESSAGE
		a8 = self.browser.find_element_by_id('cu8')
		self.assertEqual(a8.get_attribute('placeholder'),'Enter Your Message Here')
		a8.send_keys('Good day')
		time.sleep(1)


      	# SUBMIT
		btnSubmit = self.browser.find_element_by_id('btnSubmit')
		btnSubmit.click()
		time.sleep(1)
		
		# TABLE
		# table = self.browser.find_element_by_id('entryTable')
		# row_data = table.find_elements_by_tag_name('tr')
		# self.assertIn('1: INQUIRY, Gabrielle, Estropigan, 20, gstrpgn@gmail.com, 09563207021, OFFICE, USG,', [row.text for row in row_data])

	
	def test_start_list_and_retrieve_2(self):

		# BROWSER, TITLE, AND HEADER
		self.browser.get(self.live_server_url)
		self.assertIn('TMTK', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Us', headerText)

		# INQUIRY TYPE
		a9 = self.browser.find_element_by_xpath('/html/body/form/fieldset[1]/input[1]')
		a9.click()

		# PERSONAL INFORMATION

		# FIRST NAME
		a1 = self.browser.find_element_by_id('cu1')
		self.assertEqual(a1.get_attribute('placeholder'),'Your First Name')
		a1.send_keys('Gabrielle')
		time.sleep(1)

		# LAST NAME
		a2 = self.browser.find_element_by_id('cu2')
		self.assertEqual(a2.get_attribute('placeholder'),'Your Last Name')
		a2.send_keys('Estropigan')
		time.sleep(1)

		# AGE
		a3 = self.browser.find_element_by_id('cu3')
		self.assertEqual(a3.get_attribute('placeholder'),'Your Age')
		a3.send_keys('20')
		time.sleep(1)

		# EMAIL ADDRESS
		a4 = self.browser.find_element_by_id('cu4')
		self.assertEqual(a4.get_attribute('placeholder'),'Your E-mail Address')
		a4.send_keys('gstrpgn@gmail.com')
		time.sleep(1)

		# CELLPHONE NUMBER
		a5 = self.browser.find_element_by_id('cu5')
		self.assertEqual(a5.get_attribute('placeholder'),'Your Cellphone Number')
		a5.send_keys('09563207021')
		time.sleep(1)

		# ORGANIZATION
		a6= self.browser.find_element_by_id('cu6')
		self.assertEqual(a6.get_attribute('placeholder'),'Organization')
		selecta6 = Select(a6)
		selecta6.select_by_visible_text('OFFICE')
		time.sleep(1)

		# NAME OF ORGANIZATION
		a7 = self.browser.find_element_by_id('cu7')
		self.assertEqual(a7.get_attribute('placeholder'),'Enter Name of Organization')
		a7.send_keys('USG')
		time.sleep(1)

		# MESSAGE
		a8 = self.browser.find_element_by_id('cu8')
		self.assertEqual(a8.get_attribute('placeholder'),'Enter Your Message Here')
		a8.send_keys('Good day')
		time.sleep(1)


      	# SUBMIT
		btnSubmit = self.browser.find_element_by_id('btnSubmit')
		btnSubmit.click()
		time.sleep(1)


		self.browser.get(self.live_server_url)
		self.assertIn('TMTK', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Us', headerText)

		# INQUIRY TYPE
		a9 = self.browser.find_element_by_xpath('/html/body/form/fieldset[1]/input[1]')
		a9.click()

		# PERSONAL INFORMATION

		# FIRST NAME
		a1 = self.browser.find_element_by_id('cu1')
		self.assertEqual(a1.get_attribute('placeholder'),'Your First Name')
		a1.send_keys('Gerard')
		time.sleep(1)

		# LAST NAME
		a2 = self.browser.find_element_by_id('cu2')
		self.assertEqual(a2.get_attribute('placeholder'),'Your Last Name')
		a2.send_keys('Tan')
		time.sleep(1)

		# AGE
		a3 = self.browser.find_element_by_id('cu3')
		self.assertEqual(a3.get_attribute('placeholder'),'Your Age')
		a3.send_keys('55')
		time.sleep(1)

		# EMAIL ADDRESS
		a4 = self.browser.find_element_by_id('cu4')
		self.assertEqual(a4.get_attribute('placeholder'),'Your E-mail Address')
		a4.send_keys('gerardestropigan@gmail.com')
		time.sleep(1)

		# CELLPHONE NUMBER
		a5 = self.browser.find_element_by_id('cu5')
		self.assertEqual(a5.get_attribute('placeholder'),'Your Cellphone Number')
		a5.send_keys('09339298997')
		time.sleep(1)

		# ORGANIZATION
		a6= self.browser.find_element_by_id('cu6')
		self.assertEqual(a6.get_attribute('placeholder'),'Organization')
		selecta6 = Select(a6)
		selecta6.select_by_visible_text('SCHOOL/UNIVERSITY')
		time.sleep(1)

		# NAME OF ORGANIZATION
		a7 = self.browser.find_element_by_id('cu7')
		self.assertEqual(a7.get_attribute('placeholder'),'Enter Name of Organization')
		a7.send_keys('TUP')
		time.sleep(1)

		# MESSAGE
		a8 = self.browser.find_element_by_id('cu8')
		self.assertEqual(a8.get_attribute('placeholder'),'Enter Your Message Here')
		a8.send_keys('Hello Philippines')
		time.sleep(1)


      	# SUBMIT
		btnSubmit = self.browser.find_element_by_id('btnSubmit')
		btnSubmit.click()
		time.sleep(1)
		
		
		# TABLE
		table = self.browser.find_element_by_id('entryTable')
		row_data = table.find_elements_by_tag_name('tr')
		self.assertIn('1: INQUIRY, Gabrielle, Estropigan, 20, gstrpgn@gmail.com, 09563207021, OFFICE, USG, Good day', [row.text for row in row_data])
		self.assertIn('2: INQUIRY, Gerard, Tan, 55, gerardestropigan@gmail.com, 09339298997, SCHOOL/UNIVERSITY, TUP, Hello Philippines', [row.text for row in row_data])
		



# if __name__ == '__main__' :
# 	unittest.main(warnings='ignore')