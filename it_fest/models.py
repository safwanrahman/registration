from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registration(models.Model):
	GAME_CHOICE = (('Call Of Duty 4','Call Of Duty 4'),
		('Fifa 17', 'Fifa 17'),
		('NFS Most Wanted', 'NFS Most Wanted'),)
	game_name = models.CharField(max_length=15, choices=GAME_CHOICE)
	transaction_id = models.BigIntegerField()
	bkash_mobile_number = models.CharField(max_length=14)

	def __unicode__(self):
		return self.game_name

class Participant(models.Model):
	registration = models.ForeignKey('registration', null=True)
	full_name = models.CharField(max_length=100)
	email = models.EmailField()
	mobile_number = models.CharField(max_length=14)
	institute = models.CharField(max_length=100)

	def __unicode__(self):
		return self.full_name
		