# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Option(models.Model):
	option = models.TextField()

class MenuOption(models.Model):
	image =  models.ImageField(upload_to='static/img')
	name = models.TextField()
	description = models.TextField()
	price = models.FloatField()
	types = models.ForeignKey(Option)

class Book(models.Model):
	name = models.TextField()
	telephone = models.CharField(max_length=12)
	email = models.EmailField()

	date = models.DateField()
	time = models.TimeField()
	people = models.IntegerField()
	comments = models.TextField()

	def __str__(self):
		return '{} {} {}'.format(self.name, self.date, self.time)

class Dishes(models.Model):
	BREAKFAST = 'BR'
	LUNCH = 'CH'
	DINNER = 'DN'
	DISH_CHOICES = (
    	(BREAKFAST, 'Breakfast'),
    	(LUNCH, 'Lunch'),
    	(DINNER, 'Dinner'),
    )
	name = models.TextField()
	image = models.ImageField(upload_to='static/img')
	description = models.CharField(max_length=100)
	price = models.CharField(max_length=12)
	available = models.BooleanField(default=True)
	category = models.CharField(max_length=2, choices=DISH_CHOICES)


	def __str__(self):
		return '{} (${})'.format(self.name, self.price)

class Tables(models.Model):
	table = models.IntegerField(primary_key=True)
	available = models.BooleanField(default=True)

	def __str__(self):
		return 'No.{}, Available:{}'.format(self.table, self.available)

class Order(models.Model):
	PAYED = 'payed'
	PREPARED = 'ready'
	PENDING = 'pending'
	ORDER_STATUS = (
    	(PAYED, 'Payed'),
    	(PREPARED, 'Ready'),
    	(PENDING, 'Pending'),
    )

	table = models.ForeignKey('Tables', on_delete=models.CASCADE, null=True )
	dish = models.ForeignKey('Dishes', on_delete=models.CASCADE, default="01", )
	quantity = models.IntegerField()
	category = models.CharField(choices=ORDER_STATUS, max_length=7, default="pending")

class Customers(models.Model):
	idNumber = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	table = models.ForeignKey('Tables', on_delete=models.CASCADE, null=True )

	def __str__(self):
		return '{} {}'.format(self.name, self.last_name)
