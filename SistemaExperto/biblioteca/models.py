from django.db import models

class Imperativo(models.Model):
	nombre = models.CharField(max_length = 40)

class Lenguajes(models.Model):
	nombre = models.CharField(max_length = 40)
	tipo = models.CharField(max_length = 40)

class Tipos(models.Model):
	nombre = models.CharField(max_length = 40)
	tipo1 = models.CharField(max_length = 40)
	
	
	
