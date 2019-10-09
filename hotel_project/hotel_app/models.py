from django.db import models
from django.contrib.auth.models import User
import datetime

import random
# Create your models here.
class UserProfileInfo(models.Model):
	user=models.OneToOneField(User,on_delete=True)
	# additional
	portfolio_Site= models.URLField(blank=True)
	profile_pic=models.ImageField(upload_to='profile_pics', blank=True)

	def __str__(self):
		return self.user.username



class CustomerInfo(models.Model):
	customer_id = models.IntegerField()
	customer_name = models.CharField(max_length=100)
	date = models.DateField()
	ROOM_CHOICES = (
		('S', 'Standard'),
		('D', 'Delux'),
		('SD', 'Super Delux'),
		('PD', 'Premier Delux'),
		('ES', 'Executive Suit'),
		('JS', 'Junior Suit'),
		('HS', 'Honeymoon Suit'),
	)
	room_type = models.CharField(max_length=1, choices=ROOM_CHOICES)
	number_room = models.IntegerField()
	number_days= models.IntegerField()

	def __str__(self):
		return self.customer_name
