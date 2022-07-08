from django.db import models


class User (models.Model):
	firstName = models.CharField (blank=True, max_length= 25)
	lastName = models.CharField (blank=True, max_length= 25)

	userType_choices = (
		('student', 'STUDENT'),
		('teacher', 'TEACHER'),
		('conCreator', 'CONTENT CREATOR'),
		('others', 'Others')
		)
	userType = models.CharField(max_length=100, choices=userType_choices, null=True)
	organization = models.CharField(max_length=100)

	contactNumber = models.CharField(blank=True, max_length= 11)
	emailAddress = models.EmailField (blank=True)
	homeAddress = models.CharField(blank=True, max_length= 250)
class meta:
	db_table = "usertable"


class Gadget (models.Model):
	typeG = models.CharField(max_length=100)
	gadgetname = models.CharField (blank=True , max_length= 100)
	quantity = models.CharField(max_length=100)
	mesCon = models.TextField (blank=True)
# class BudgetLog (models.Model):
# 	userID = models.ForeignKey (User, on_delete=models.CASCADE)
# 	productID = models.ForeignKey (Gadget, on_delete=models.CASCADE)
# 	dateLog = models.DateField (blank=True)
# 	amountLog = models.CharField (blank=True, max_length= 6)
# 	remBalance = models.CharField (blank=True, max_length= 6)
# 	totBudget = models.CharField (blank=True, max_length= 6)

# 	suggestion_choices = (
# 		('proceed to order', 'ORDER NOW'),
# 		('not enough', 'NOT ENOUGH BUDGET'),
# 		)
# 	suggestion = models.CharField(max_length=100, choices=suggestion_choices, null=True)


# class Order (models.Model):

# 	userID = models.ForeignKey(User, on_delete=models.CASCADE) 
# 	productID = models.ForeignKey(Gadget, on_delete=models.CASCADE) 
# 	# logID = models.ForeignKey(BudgetLog, on_delete=models.CASCADE)

class Delivery (models.Model):
	dateOrder= models.CharField(max_length=100)
	delProcess = models.CharField(max_length=100)
	modPay = models.CharField(max_length=100)
	cash = models.CharField (blank=True , max_length= 12)

class Summary(models.Model):
	user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
	gadget = models.ForeignKey(Gadget, default=None, on_delete=models.CASCADE)
	delivery = models.ForeignKey(Delivery, default=None, on_delete=models.CASCADE)




# class Message (models.Model):
# 	uid = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
# 	mesType_choices = (
# 		('inquiry', 'INQUIRY'),
# 		('comment', 'COMMENT'),
# 		('suggestion', 'SUGGESTION'),
# 		)	 
# 	mesType = models.CharField(max_length=100, choices=mesType_choices, null=True)
# 	ratings = models.CharField (blank=True, max_length= 100)


