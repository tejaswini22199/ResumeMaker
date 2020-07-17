from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
from django.views.generic import ListView,DetailView
from django.urls import reverse

default_user_id =1
class Category(models.Model):
	name=models.CharField(max_length=255)
	def __str__(self):
		return self.name
class contactdetails(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE,default=default_user_id)
	resume_name = models.CharField(max_length=100,default='resume')
	full_name= models.CharField(max_length=55)
	position= models.CharField(max_length=30)
	city= models.CharField(max_length=30)
	state= models.CharField(max_length=30)
	zipcode= models.CharField(max_length=10)
	phone= models.CharField(max_length=12)
	email= models.EmailField(max_length=40)
	personal_profile = models.CharField(max_length=1000)



class educ(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE,default=default_user_id)
	resume_name = models.CharField(max_length=100,default='resume')
	school_name = models.CharField(max_length=55)
	school_location = models.CharField(max_length=55)
	Degree = models.CharField(max_length=55)
	CGPA=models.CharField(max_length=55)
	Field_of_Study = models.CharField(max_length=55)
	Expected_year_of_grad = models.CharField(max_length=55)


	def __str__(self):
		return self.school_name+'|'+ str(self.school_location)
	
	def get_absolute_url (self):
		return reverse ('education')

class workexp(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE,default=default_user_id)
	resume_name = models.CharField(max_length=100,default='resume')
	job_title = models.CharField(max_length=55)
	employer = models.CharField(max_length=55)
	city = models.CharField(max_length=55)
	state=models.CharField(max_length=55)
	#startdate = models.DateField(max_length=55,null=True)
	#enddate = models.DateField(max_length=55,null=True)
	jobdesc = models.CharField(max_length=2000)

	def __str__(self):
		return self.job_title+'|'+ self.city
	
	def get_absolute_url (self):
		return reverse ('job')
		

class skills(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE,default=default_user_id)
	resume_name = models.CharField(max_length=100,default='resume')
	skill= models.CharField(max_length=55)


	#below code is added by siri.
	def __str__(self):
		return self.skill
	
	def get_absolute_url (self):
		return reverse ('skillsview')
		

class extrafield(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE,default=default_user_id)
	resume_name = models.CharField(max_length=100,default='resume')
	field_name = models.CharField(max_length=100)
	explanation = RichTextField(blank=True ,null= True)

	def get_absolute_url (self):
		return reverse ('extrafi')

		