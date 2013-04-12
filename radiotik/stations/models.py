from django.db import models

from radiotik.stations.functions import make_upload_path

LANGUAGE_CHOICES = (
	('1', 'Español'),
	('2', 'Inglés'),
	)

TIME_CHOICES = (
	('1','Zona1'),
	('2','Zona2'),
	('3','Zona3'),
	('4','Zona4'),
	)

class Station(models.Model):
	name = models.CharField(max_length=255)
	slogan = models.CharField(max_length=255)
	picture = models.ImageField(upload_to=make_upload_path)
	language = models.CharField(max_length=255, choices=LANGUAGE_CHOICES)
	time_zone = models.CharField(max_length=124, choices=TIME_CHOICES)

	def __unicode__(self):
		return u'%s' % (self.name)