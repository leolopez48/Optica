# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.forms import TextInput, Textarea 
from django.db import models

# Register your models here.
class ClinicaConsulta(admin.ModelAdmin): 
	formfield_overrides = { 
		models.CharField: {'widget': TextInput(attrs={'size':'20'})}, 
		models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})}, 
	} 

