# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Gmc(models.Model):
	gmc_name = models.CharField(max_length=50, unique=True)
	
	def __str__(self):
		return self.gmc_name

class Ldp(models.Model):
	
	site_name = models.CharField(max_length=100)
	ldp_code = models.CharField(max_length=50, unique=True)
	gmc = models.ForeignKey('Gmc', blank=True)
	
	def __str__(self):
		return self.ldp_code

# class Ods(models.Model):
# 	ods_code = models.CharField(max_length=50, unique=True)
# 	ldp = models.ForeignKey('Ldp')
	
# 	def __str__(self):
# 		return self.ods_code

# class LdapGroup(models.Model):
# 	name = models.CharField(max_length=50, unique=True)
	
# 	def __str__(self):
# 		return self.name

