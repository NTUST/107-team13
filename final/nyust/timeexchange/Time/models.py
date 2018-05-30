from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Member(models.Model):
	accountID=models.AutoField(primary_key=True)
	account=models.CharField(max_length=100,blank=False,null=False)
	password=models.CharField(max_length=20,validators=[MinLengthValidator(4)],blank=False,null=False)
	name=models.CharField(max_length=100,blank=False,null=False)
	email=models.EmailField(max_length=100,blank=False,null=False)
	birthday=models.DateField()
	GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	phonenumber=models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.account
class Seller(models.Model):
	member=models.ForeignKey(Member,on_delete=models.CASCADE)
	courseID=models.AutoField(primary_key=True)
	coursename=models.CharField(max_length=100)
	pub_date=models.DateTimeField()
	def __str__(self):
		return self.coursename
class Buyer(models.Model):
	member=models.ForeignKey(Member,on_delete=models.CASCADE)
	course=models.ForeignKey(Seller,on_delete=models.CASCADE)
	buyID=models.AutoField(primary_key=True)
	buy_date=models.DateTimeField()
	def __str__(self):
		return self.buyID