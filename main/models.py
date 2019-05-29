from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
	name=models.CharField(max_length=100)
	logo=models.ImageField()
	address=models.CharField(max_length=200)

	def __str__(self):
		return self.name

class UserProfile(models.Model):
    user   = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(default='/happyprofile.jpg')
    job=models.CharField(max_length=100)
    company=models.OneToOneField(Company,on_delete=models.SET_NULL,null=True)

    def __str__(self):
    	return self.user.username




