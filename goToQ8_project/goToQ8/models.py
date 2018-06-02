from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField

category_choises = (
	('children', 'children'),
	('shopping', 'shopping'),
	('soprts', 'soprts'),
	('restaurants', 'restaurants'),
	('entertainment', 'entertainment'),
	('theaters', 'theaters'),
	('cinema', 'cinema'),
	('concerts', 'concerts'),
	('festivals', 'festivals'),
	('trips', 'trips'),
	('seminars', 'seminars'),
	)

# Create your models here.
class Event(models.Model):
	title= models.CharField(max_length=200)
	description = models.TextField()
	image= models.ImageField(null=True, blank=True)
	publish_date= models.DateField(auto_now_add=True)
	event_date= models.DateTimeField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	color = ColorField(default='#FF0000')
	category = models.CharField(max_length=200 , choices=category_choises, null=True)
	hot_and_trend= models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Plan(models.Model):
	title= models.CharField(max_length=200, null=True)
	weekend_date= models.DateField()
	plans = models.ManyToManyField(Event)
	planner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title

class Favourite(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Profile(models.Model):
	username = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	plans = models.ForeignKey(Plan, blank=True, null=True, on_delete=models.CASCADE)
	events = models.ManyToManyField(Event, blank=True) 
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	dob = models.DateField()
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		if self.username==None:
			return "ERROR-CUSTOMER NAME IS NULL"
		return self.username



class Friends(models.Model):
	name = models.CharField(max_length=200)
	logo = models.ImageField(null=True, blank=True)
	phone_number = models.IntegerField(blank=True, null=True)
	location= models.CharField(max_length=500, null=True)
	website= models.URLField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.name
	