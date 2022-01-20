from django.db import models


class Items(models.Model):
	name = models.CharField(max_length=191,default="", editable=False)
	price = models.TextField(max_length=50,default="", editable=False)
