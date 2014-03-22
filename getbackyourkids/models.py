from django.db import models

# Create your models here.
class Contacts(models.Model):
	Name = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)

class Comments(models.Model):
	Name = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)
	Comments = models.CharField(max_length=2000)
		
class Counters(models.Model):
	Page1Submit = models.FloatField()
	Page2Submit = models.FloatField()
	PageHitCount = models.FloatField()
	Video1 = models.FloatField()
	Video2 = models.FloatField()
	Video3 = models.FloatField()
	Video4 = models.FloatField()
	Counter1 = models.FloatField()
	Counter2 = models.FloatField()
    