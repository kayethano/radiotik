# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User 
from django.db import models
from django.db.models.signals import post_save

from django_facebook.models import FacebookProfileModel

COUNTRY_CHOICES = (

	('1', 'México'),
	('2', 'Estados Unidos'),
	('3', 'Brasil'),
	('4', 'Argentina'),
	('5', 'Chile'),
	('6', 'Guatemala'),
	('7', 'El Salvador'),

	)

LANGUAGE_CHOICES = (
	('1', 'Español'),
	('2', 'Inglés'),
	)

class Profile(FacebookProfileModel):
	user = models.OneToOneField(User)
	country = models.CharField(max_length=25, choices=COUNTRY_CHOICES)
	city = models.CharField(max_length=25)
	language = models.CharField(max_length=25, choices=LANGUAGE_CHOICES)

	def __unicode__(self):
		return u'%s' % (self.user)

	#Create profile when new user
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	post_save.connect(create_user_profile, sender=User)
