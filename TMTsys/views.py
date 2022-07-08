from django.shortcuts import render, redirect
from .models import *


# def MainPage(request):

# 	return render (request, 'index.html')

# NAVIGATION

def homepage(request):
	return render (request, 'index.html')

def laptop(request):
	return render (request, 'laptop.html')

def monitor(request):
	return render (request, 'monitor.html')

def mouse(request):
	return render (request, 'mouse.html')
	
def keyboard(request):
	return render (request, 'keyboard.html')

#forms

def checkout1(request):

	if request.method == "POST":
		user = User.objects.create(firstName=request.POST['firstName'],
			lastName=request.POST['lastName'],
			userType=request.POST['userType'],
			organization=request.POST['organization'],
			contactNumber=request.POST['contactNumber'],
			emailAddress=request.POST['emailAddress'],
			homeAddress=request.POST['homeAddress'],)
		user.save()
		return redirect(f'/checkout2/{user.id}')

	return render(request, 'checkout1.html')

def checkout2(request,userID):
	user = User.objects.get(id=userID)
	if request.method == "POST":
		gadget = Gadget.objects.create(typeG = request.POST['typeg'],
			gadgetname = request.POST['gadgetname'],
			quantity = request.POST['qty'],
			mesCon= request.POST['mesCon'])
		gadget.save()

		return redirect(f'/checkout3/{user.id}/{gadget.id}')
	else:
		return render(request, 'checkout2.html')

def checkout3(request,userID,gadgetID):
	user = User.objects.get(id=userID)
	gadget = Gadget.objects.get(id=gadgetID)

	if request.method == "POST":
		deliverys = Delivery.objects.create(dateOrder=request.POST['DateToday'],
			delProcess=request.POST['ModDel'],
			modPay=request.POST['ModPay'],
			cash=request.POST['CASH'],)
		deliverys.save()

		summary = Summary.objects.create(user=user,
			gadget=gadget, delivery=deliverys)

		summary.save()
		return redirect(f'/checkout4/{user.id}')
	else:
		return render(request, 'checkout3.html')

def checkout4(request,userID):
	user = User.objects.get(id=userID)
	# gadget = Gadget.objects.get(id=gadgetID)
	# delivery = Delivery.objects.get(id=delID)
	summary = Summary.objects.all()
	if request.method == "POST":
		pass
	else:
		return render(request, 'checkout4.html', {"sum":summary})

def delete(request, userID,itemID):
	userno = User.objects.get(id=userID)
	summary = Summary.objects.get(id=itemID)
	summary.delete()

	return redirect(f'/checkout4/{userno.id}')


def showUser(request,userID):
	useno =  User.objects.get(id=userID)
	if request.method=='POST':
		gadget = Gadget.objects.create(typeG=request.POST['typeg'],gadgetname=request.POST['gadgetname'],
			quantity=request.POST['qty'],mesCon=request.POST['mesCon'])

		gadget.save()
		return redirect(f'/TMTsys/{useno.id}/{gadget.id}/checkout3')
	else:
		return render(request, 'checkout2.html',{'useno':useno})

def addUser(request):
	fname = request.POST['firstName']
	lname = request.POST['lastName']
	utype = request.POST['userType']
	org = request.POST['organization']
	cnum = request.POST['contactNumber']
	email = request.POST['emailAddress']
	add = request.POST['homeAddress']
	newUser = User.objects.create(
		firstName=fname,
		lastName=lname,
		userType=utype,
		organization=org,
		contactNumber=cnum,
		emailAddress=email,
		homeAddress=add)	
	return redirect(f'/TMTsys/{newUser.id}/')


def editInfo(request, userID, itemID):
	user =  User.objects.get(id=userID)
	summary = Summary.objects.get(id=itemID)

	if request.method == "POST":
		user.firstName = request.POST['firstName']
		user.lastName = request.POST['lastName']
		user.userType = request.POST['userType']
		user.contactNumber = request.POST['contactNumber']
		user.emailAddress = request.POST['emailAddress']
		user.homeAddress = request.POST['homAddress']
		user.organization = request.POST['organization']

		user.save()

		return redirect(f'/checkout4/{user.id}')

	else:

		return render(request,'checkout5.html', {'user':user,'summary':summary})

def updateInfo(request, userID):
	user =  User.objects.filter(id=userID)
	user.firstName = request.POST['firstName']
	user.lastName = request.POST['lastName']
	user.userType = request.POST['userType']
	user.organization = request.POST['organization']
	user.contactNumber = request.POST['contactNumber']
	user.emailAddress = request.POST['emailAddress']
	user.homeAddress = request.POST['homeAddress']
	user.save()	

	return redirect(f'/TMTsys/{userID}/checkout4')

# def checkout2(request):
# 	return render(request, 'checkout2.html')

# def checkout3(request, userID, gadgetID):
# 	useno =  User.objects.get(id=userID)
# 	gadget = Gadget.objects.get(id=gadgetID)

# 	if request.method == "POST":
# 		delivery = Delivery.objects.create(
# 			 dateOrder = request.POST['DateToday'],
# 			delProcess=request.POST['ModDel'], modPay = request.POST['ModPay'],
# 			cash=request.POST['CASH']
# 			)

# 		Summary.objects.create(user=useno, gadget=gadget, delivery=delivery)

# 		return redirect(f'/TMTsys/checkout4/{useno.id}')

# 	return render(request, 'checkout3.html')

# def checkout4(request, userID):
# 	useno =  User.objects.get(id=userID)
# 	lists = Summary.objects.filter(user=userID)
# 	return render(request, 'checkout4.html',{'list':lists})

def checkout5(request):
	return render(request, 'checkout5.html')


def contact(request):
	return render (request, 'contact.html')

def feedback(request):
	return render (request, 'feedback.html')



# BRANDS

def laptopAsus(request):
	return render (request, 'laptopAsus.html')

def laptopLenovo(request):
	return render (request, 'laptopLenovo.html')

def laptopDell(request):
	return render (request, 'laptopDell.html')


def monitorNVision(request):
	return render (request, 'monitorNVision.html')

def monitorAsus(request):
	return render (request, 'monitorAsus.html')

def monitorAcer(request):
	return render (request, 'monitorAcer.html')


def mouseRazer(request):
	return render (request, 'mouseRazer.html')

def mouseLogitech(request):
	return render (request, 'mouseLogitech.html')

def mouseSteel(request):
	return render (request, 'mouseSteel.html')


def keyboardLogitech(request):
	return render (request, 'keyboardLogitech.html')

def keyboardRazer(request):
	return render (request, 'keyboardRazer.html')

def keyboardCorsair(request):
	return render (request, 'keyboardCorsair.html')


# LAPTOPS

# ASUS LAPTOPS
def asusL1(request):
	return render (request, 'asusL1.html')

def asusL2(request):
	return render (request, 'asusL2.html')

def asusL3(request):
	return render (request, 'asusL3.html')

def asusL4(request):
	return render (request, 'asusL4.html')

def asusL5(request):
	return render (request, 'asusL5.html')


# LENOVO LAPTOPS

def lenovoL1(request):
	return render (request, 'lenovoL1.html')

def lenovoL2(request):
	return render (request, 'lenovoL2.html')

def lenovoL3(request):
	return render (request, 'lenovoL3.html')

def lenovoL4(request):
	return render (request, 'lenovoL4.html')

def lenovoL5(request):
	return render (request, 'lenovoL5.html')


# DELL LAPTOPS

def dellL1(request):
	return render (request, 'dellL1.html')

def dellL2(request):
	return render (request, 'dellL2.html')

def dellL3(request):
	return render (request, 'dellL3.html')

def dellL4(request):
	return render (request, 'dellL4.html')

def dellL5(request):
	return render (request, 'dellL5.html')


# MONITORS

# NVISION MONITORS

def nvisionMON1(request):
	return render (request, 'nvisionMON1.html')

def nvisionMON2(request):
	return render (request, 'nvisionMON2.html')

def nvisionMON3(request):
	return render (request, 'nvisionMON3.html')

def nvisionMON4(request):
	return render (request, 'nvisionMON4.html')

def nvisionMON5(request):
	return render (request, 'nvisionMON5.html')


# ASUS MONITORS

def asusMON1(request):
	return render (request, 'asusMON1.html')

def asusMON2(request):
	return render (request, 'asusMON2.html')

def asusMON3(request):
	return render (request, 'asusMON3.html')

def asusMON4(request):
	return render (request, 'asusMON4.html')

def asusMON5(request):
	return render (request, 'asusMON5.html')


# ACER MONITORS

def acerMON1(request):
	return render (request, 'acerMON1.html')

def acerMON2(request):
	return render (request, 'acerMON2.html')

def acerMON3(request):
	return render (request, 'acerMON3.html')

def acerMON4(request):
	return render (request, 'acerMON4.html')

def acerMON5(request):
	return render (request, 'acerMON5.html')


# MOUSE

# RAZER MOUSE
def razerMOU1(request):
	return render (request, 'razerMOU1.html')

def razerMOU2(request):
	return render (request, 'razerMOU2.html')

def razerMOU3(request):
	return render (request, 'razerMOU3.html')

def razerMOU4(request):
	return render (request, 'razerMOU4.html')

def razerMOU5(request):
	return render (request, 'razerMOU5.html')


# LOGITECH MOUSE
def logiMOU1(request):
	return render (request, 'logiMOU1.html')

def logiMOU2(request):
	return render (request, 'logiMOU2.html')

def logiMOU3(request):
	return render (request, 'logiMOU3.html')

def logiMOU4(request):
	return render (request, 'logiMOU4.html')

def logiMOU5(request):
	return render (request, 'logiMOU5.html')


# STEELSERIES MOUSE
def steelMOU1(request):
	return render (request, 'steelMOU1.html')

def steelMOU2(request):
	return render (request, 'steelMOU2.html')

def steelMOU3(request):
	return render (request, 'steelMOU3.html')

def steelMOU4(request):
	return render (request, 'steelMOU4.html')

def steelMOU5(request):
	return render (request, 'steelMOU5.html')


# KEYBOARD

# LOGITECH KEYBOARD
def logiKEY1(request):
	return render (request, 'logiKEY1.html')

def logiKEY2(request):
	return render (request, 'logiKEY2.html')

def logiKEY3(request):
	return render (request, 'logiKEY3.html')

def logiKEY4(request):
	return render (request, 'logiKEY4.html')

def logiKEY5(request):
	return render (request, 'logiKEY5.html')


# RAZER KEYBOARD

def razerKEY1(request):
	return render (request, 'razerKEY1.html')

def razerKEY2(request):
	return render (request, 'razerKEY2.html')

def razerKEY3(request):
	return render (request, 'razerKEY3.html')

def razerKEY4(request):
	return render (request, 'razerKEY4.html')

def razerKEY5(request):
	return render (request, 'razerKEY5.html')


# CORSAIR KEYBOARD

def corKEY1(request):
	return render (request, 'corKEY1.html')

def corKEY2(request):
	return render (request, 'corKEY2.html')

def corKEY3(request):
	return render (request, 'corKEY3.html')

def corKEY4(request):
	return render (request, 'corKEY4.html')

def corKEY5(request):
	return render (request, 'corKEY5.html')
