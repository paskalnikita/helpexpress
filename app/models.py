"""
Definition of models.
"""

from django.db import models




class Form(models.Model):
    name_surname =  models.CharField(max_length=512)
    email =  models.CharField(max_length=512)
    phone =  models.CharField(max_length=512)
    message =  models.CharField(max_length=512)
