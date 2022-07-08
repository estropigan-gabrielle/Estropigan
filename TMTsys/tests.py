from django.test import TestCase
from TMTsys.views import MainPage
from TMTsys.models import PersonalInfo


# from django.http import HttpRequest
# from django.template.loader import render_to_string
# from django.urls import resolve


class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/',{
			'favs':'INQUIRY',
			'cu1a':'GABRIELLE',
			'cu1b':'ESTROPIGAN',
			'cu1c':'20',
			'cu1d':'gabrielle.estropigan@gsfe.tupcavite.edu.ph',
			'cu1e':'09563207021',
			'cu1f':'OFFICE',
			'cu1g':'USG',
			'cu1h':'Hello World',})

		self.assertEqual(PersonalInfo.objects.count(),1)
		newData = PersonalInfo.objects.first()
		self.assertEqual(newData.option1, 'INQUIRY')
		self.assertEqual(newData.fname, 'GABRIELLE')
		self.assertEqual(newData.lname, 'ESTROPIGAN')
		self.assertEqual(newData.age, 20)
		self.assertEqual(newData.email, 'gabrielle.estropigan@gsfe.tupcavite.edu.ph')	
		self.assertEqual(newData.celno, '09563207021')
		self.assertEqual(newData.org, 'OFFICE')
		self.assertEqual(newData.orgn, 'USG')
		self.assertEqual(newData.message, 'Hello World')

		# self.assertEqual(Message.objects.count(),1)
		# newData2 = Message.objects.first()
		# self.assertEqual(newData2.message, 'Hello World')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(PersonalInfo.objects.count(), 0)
		# self.assertEqual(Message.objects.count(), 0)

class ORMTEST (TestCase):

	def test_saving_retriv(self):

		copy_of_PersonalInfo = PersonalInfo()
		copy_of_PersonalInfo.option1 ='INQUIRY'
		copy_of_PersonalInfo.fname ='GABRIELLE'
		copy_of_PersonalInfo.lname ='ESTROPIGAN'
		copy_of_PersonalInfo.age = 20
		copy_of_PersonalInfo.email ='gabrielle.estropigan@gsfe.tupcavite.edu.ph'
		copy_of_PersonalInfo.celno ='09563207021'
		copy_of_PersonalInfo.org = 'OFFICE'
		copy_of_PersonalInfo.orgn = 'USG'
		copy_of_PersonalInfo.message ='Hello World'
		copy_of_PersonalInfo.save ()

		# copy_of_Message = Message()
		# copy_of_Message.message = 'Hello World'
		# copy_of_Message.save()

		obj_PersonalInfo = PersonalInfo.objects.all()
		self.assertEqual(obj_PersonalInfo.count(),1)
		self.assertEqual(obj_PersonalInfo[0].option1,'INQUIRY')
		self.assertEqual(obj_PersonalInfo[0].fname,'GABRIELLE')
		self.assertEqual(obj_PersonalInfo[0].lname,'ESTROPIGAN')
		self.assertEqual(obj_PersonalInfo[0].age,20)
		self.assertEqual(obj_PersonalInfo[0].email,'gabrielle.estropigan@gsfe.tupcavite.edu.ph')
		self.assertEqual(obj_PersonalInfo[0].celno,'09563207021')
		self.assertEqual(obj_PersonalInfo[0].org,'OFFICE')
		self.assertEqual(obj_PersonalInfo[0].orgn,'USG')
		self.assertEqual(obj_PersonalInfo[0].message,'Hello World')

		# obj_Message = Message.objects.all()
		# self.assertEqual(obj_Message.count(),1)
		# self.assertEqual(obj_Message[0].message,'Hello World')


	def test_template_display_list(self):

		PersonalInfo.objects.create(
			option1 = 'INQUIRY',
			fname = 'GABRIELLE',
			lname = 'ESTROPIGAN',
			age = 20, 
			email = 'gabrielle.estropigan@gsfe.tupcavite.edu.ph',
			celno = '09563207021',
			org = 'OFFICE',
			orgn = 'USG',
			message = 'Hello World')
		# Message.objects.create(
		# 	message = 'Hello World')

		PersonalInfo.objects.create(
			option1 = 'SUGGESTION',
			fname = 'ALUDIA',
			lname = 'PONESTO',
			age = 46, 
			email = 'alodiaponesto23@gmail.com',
			celno = '09339298997',
			org = 'SCHOOL',
			orgn = 'DNHS',
			message = 'Hello Earth')
		# Message.objects.create(
		# 	message = 'Hello Earth')

		response = self.client.get('/')
		self.assertIn('1: INQUIRY, GABRIELLE, ESTROPIGAN, 20, gabrielle.estropigan@gsfe.tupcavite.edu.ph, 09563207021, OFFICE, USG,',
		response.content.decode())

		

	# def test_responding_post_request(self):
	# 	resp = self.client.post('/', 
	# 		data={
	# 		'INQUIRY':'b9',
	# 		'cu1': 'b1',
	# 		'cu2': 'b2',
	# 		'cu3': 'b3',
	# 		'cu4': 'b4',
	# 		'cu5': 'b5',
	# 		'cu6': 'b6',
	# 		'cu7': 'b7',
	# 		'cu8': 'b8'})
	# 	self.assertIn('INQUIRY', resp.content.decode())
	# 	self.assertTemplateUsed(resp, 'mainpage.html')