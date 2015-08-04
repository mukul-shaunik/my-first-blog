from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
class RegForm(models.Model):
	name = models.CharField(max_length=200)
	dob = models.DateTimeField(default=timezone.now)
	email_id = models.CharField(max_length=200)
	father_name = models.CharField(max_length=200)
	mother_name = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	p_address = models.TextField()
	def getName(self):
		return self.name
	def getDob(self):
		return self.dob
	def getEmail_id(self):
		return self.email_id
	def getFather_name(self):
		return self.father_name
	def getMother_name(self):
		return self.mother_name
	def getCity(self):
		return self.city
	def getState(self):
		return self.state
	def getAddress(self):
		return self.p_address
	def setName(self,name):
		return self.name
	def setDob(self,dob):
		return self.dob
	def setEmail_id(self,email_id):
		return self.email_id
	def setFather_name(self,father_name):
		return self.father_name
	def setMother_name(self,mother_name):
		return self.mother_name
	def setCity(self,city):
		self.city=city
	def setState(self,state):
		return self.state
	def setAddress(self,p_address):
		return self.p_address
	def __str__(self):
		return self.name
